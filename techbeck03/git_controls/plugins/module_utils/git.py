from ansible.module_utils.six import iteritems
from ansible.module_utils.urls import fetch_url
from ansible.module_utils.basic import env_fallback
from pathlib import Path
from shutil import rmtree
from time import time
from typing import List, TypedDict, Text

try:
    from git import Repo
    HAS_GIT = True
except ImportError:
    HAS_GIT = False

git_argument_spec = dict(
    git_token=dict(fallback=(env_fallback, ['GIT_TOKEN']), type='str', no_log=True),
    git_username=dict(fallback=(env_fallback, ['GIT_USERNAME']), type='str'),
    git_password=dict(fallback=(env_fallback, ['GIT_PASSWORD']), type='str', no_log=True),
    repo=dict(fallback=(env_fallback, ['GIT_REPO']), type='str', required=True),
    org=dict(fallback=(env_fallback, ['GIT_ORG']), type='str', required=True),
    branch=dict(type='str', default='master'),
    working_dir=dict(type='str', required=True),
)

FileReturn = TypedDict('FileReturn', {'status': str, 'changed_files': List[str]})
CloneReturn = TypedDict('CloneReturn', {'status': str, 'working_dir': str})

class GitModule():

    def __init__(self, module):
        self.module = module
        self.result = dict(changed=False)
        if not HAS_GIT:
            self.module.fail_json(msg='GitPython is required for this module')
        # * Check for required auth parameters
        git_token = self.module.params.get('git_token')
        git_username = self.module.params.get('git_username')
        git_password = self.module.params.get('git_password')
        org = self.module.params.get('org')
        repo = self.module.params.get('repo')
        if not git_token and not git_username:
            self.module.fail_json(msg='One of `git_token` or `git_username` is required')
        if git_token and git_username:
            self.module.fail_json(msg='Only one of `git_token` or `git_username` is allowed')
        if git_username and not git_password:
            self.module.fail_json(msg='`git_password` is required with `git_username`')
        
        # * Set URL based on auth method
        if git_token:
            self.repo_url = f'https://{git_token}:x-oauth-basic@github.com/{org}/{repo}'
        else:
            self.repo_url = f'https://{git_username}:{git_password}@github.com/{org}/{repo}'

    def addFiles(self, files: List[str]) -> FileReturn:
        """Adds supplied files to git repo based on ansible provided parameters

        Args:
            files (List): List of file names within working directory to add for commit

        Returns:
            FileReturn: Dictionary containing the results from the git add
            Properties:
                - status (str): modified|unchanced
                - contents (List): List of changed filenames
        """
        workingDir = self.module.params.get("working_dir")
        repo = Repo(workingDir)
        if repo.bare:
            self.module.fail_json(msg='Working directory does not appear to contain a git repo')
        repo.index.add(items=files)
        changedFiles = [ diff.a_path for diff in repo.index.diff(repo.head.commit) ]
        if len(changedFiles) == 0:
            return dict(
                status = 'unchanged',
                changed_files = changedFiles
            )
        return dict(
            status = 'modified',
            changed_files = changedFiles
        )

    def removeFiles(self, files: List[str]) -> FileReturn:
        """Removes supplied files to git repo based on ansible provided parameters

        Args:
            files (List): List of filenames to remove from git repo

        Returns:
            FileReturn: Dictionary containing the results from the git add
            Properties:
                - status (str): modified|unchanced
                - changed_files (List): List of changed filenames
        """

        workingDir = self.module.params.get("working_dir")
        repo = Repo(workingDir)
        if repo.bare:
            self.module.fail_json(msg='Working directory does not appear to contain a git repo')
        valid_files = [ f"{workingDir}/{file}" for file in files if Path(f"{workingDir}/{file}").exists() ]
        if len(valid_files) == 0:
            return dict(
                status = 'unchanged',
                changed_files = []
            )
        repo.index.remove(valid_files, working_tree=True)
        changedFiles = [ diff.a_path for diff in repo.index.diff(repo.head.commit) ]
        if len(changedFiles) == 0:
            return dict(
                status = 'unchanged',
                changed_files = changedFiles
            )
        return dict(
            status = 'modified',
            changed_files = changedFiles
        )
    
    def commitFiles(self) -> FileReturn:
        """Commit file changes to repo

        Returns:
            FileReturn: Dictionary containing the results from the git add
            Properties:
                - status (str): modified|unchanced
                - changed_files (List): List of changed filenames
        """
        workingDir = self.module.params.get("working_dir")
        repo = Repo(workingDir)
        if repo.bare:
            self.module.fail_json(msg='Working directory does not appear to contain a git repo')
        changedFiles = [ diff.a_path for diff in repo.index.diff(repo.head.commit) ]
        if len(changedFiles) == 0:
            return dict(
                status = 'unchanged',
                changed_files = changedFiles
            )
        repo.index.commit(message=self.module.params.get("commit_string"))
        origin = repo.remote(name='origin')
        origin.push()
        return dict(
            status = 'modified',
            changed_files = changedFiles
        )
    
    def cloneRepo(self, auto_generate_parent: bool, pull: bool) -> Text:
        """Clones provided repo to local working directory

        Args:
            auto_generate_parent (bool): Creates a random parent folder for git clone if True

        Returns:
            Text: path to working directory
        """
        workingDir = Path(self.module.params.get("working_dir")) if not auto_generate_parent else Path(f'{self.module.params.get("working_dir")}/{str(int(time() * 1000))}')
        if workingDir.exists():
            repo = Repo(workingDir)
            if repo.bare or repo.remotes.origin.url != self.repo_url:
                self.module.fail_json(msg="Specified working directory already exists and doesn't contain the desired git repo")
            if pull:
                current_commit = repo.head.commit.hexsha
                origin = repo.remote(name='origin')
                origin.pull()
                repo = Repo(workingDir)
                if repo.head.commit.hexsha != current_commit:
                    return dict(
                        status = 'modified',
                        working_dir = f"{workingDir}"
                    )        
            return dict(
                status = 'unchanged',
                working_dir = f"{workingDir}"
            )
        else:
            workingDir.mkdir()
            Repo.clone_from(self.repo_url, workingDir, branch=self.module.params.get("branch"))
            return dict(
                status = 'unchanged',
                working_dir = f"{workingDir}"
            )

    def removeRepo(self) -> bool:
        """Removes working directory

        Returns:
            bool: True if working directory exists and was deleted else False
        """
        workingDir = self.module.params.get("working_dir")
        if not Path(workingDir).exists():
            return False
        rmtree(workingDir)
        return True