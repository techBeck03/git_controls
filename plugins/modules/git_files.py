#!/usr/bin/python

# Copyright: (c) 2018, Terry Jones <terry.jones@example.org>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r'''
---
module: git_files

short_description: Add, remove and commit files to existing git repo

version_added: "1.0.0"

description: This module adds, removes and commits files to a git repo clone to the specified working directory

options:
    add_files:
        description:
            - A list of filenames to be added to the specified git repo working directory
            - Filenames can be relative to the working directory
        required: false
        type: list
        elements: str
    remove_files:
        description:
            - A list of filenames to be removed from the specified git repo working directory
            - Filenames can be relative to the working directory
        required: false
        type: list
        elements: str
    commit_string:
        description:
            - The commit string used for git repo commit
        required: true
        type: str
extends_documentation_fragment:
    - git
author:
    - Brandon Beck (@techBeck03)
'''

EXAMPLES = r'''
# Clone a repo
- name: Add, Remove and Commit Files
    techbeck03.git_controls.git_clone.git_files:
        repo: "myrepo"
        org: "username"
        branch: "master"
        pull: True
        working_dir: /tmp/myrepo
        commit_string: "adding user {{ user.samAccountName }}"
        add_files:
            - "{{ user.samAccountName }}.tf"
        remove_files:
            - brhilton.tf

'''

RETURN = r'''
# These are examples of possible return values, and in general should use other names for return values.
added_files:
    description: A list of filenames added with latest commit
    type: list
    elements: str
    returned: changed
    sample: '[/tmp/myrepo]'
removed_files:
    description: A list of filenames removed with latest commit
    type: list
    elements: str
    returned: changed
    sample: '[/tmp/myrepo]'
'''

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.git import GitModule, git_argument_spec

def run_module():
    # define available arguments/parameters a user can pass to the module
    module_args = dict(
        add_files=dict(type='list', elements='str'),
        remove_files=dict(type='list', elements='path'),
        commit_string=dict(type='str', required=True),
    )
    module_args.update(git_argument_spec)

    result = dict(
        changed=False,
        added_files = [],
        removed_files = []
    )
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=False,
        required_one_of=[('add_files', 'remove_files')]
    )
    git = GitModule(module)
    add_files = module.params.get("add_files", [])
    remove_files = module.params.get("remove_files", [])

    # Handle added files
    if add_files and len(add_files) > 0:
        add_result = git.addFiles(add_files)
        if add_result["status"] == 'modified':
            result["changed"] = True
            result["added_files"] = add_result["changed_files"]    
    # Handle removed files
    if remove_files and len(remove_files) > 0:
        remove_result = git.removeFiles(remove_files)
        if not result["changed"] and remove_result["status"] == 'modified':
            result["changed"] = True
            result["removed_files"] = remove_result["changed_files"]

    if result["changed"]:
        git.commitFiles()
    
    module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()