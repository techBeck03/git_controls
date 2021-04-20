# -*- coding: utf-8 -*-

class ModuleDocFragment(object):
    # Git doc fragment
    DOCUMENTATION = '''
options:
    git_token:
        description:
            - Git token used for authentication
            - Required if I(git_username=None)
            - If not set, the value of the B(GIT_TOKEN) environment variable is used.
        type: str
        env:
            - name: GIT_TOKEN
        required: no
    git_username:
        description:
            - Username used for Github authorization
            - Required if I(git_token=None)
            - If not set, the value of the B(GIT_USERNAME) environment variable is used.
        type: str
        env:
            - name: GIT_USERNAME
        required: no
    git_password:
        description:
            - Password used for Github authorization
            - Required if I(git_token=None)
            - If not set, the value of the B(GIT_PASSWORD) environment variable is used.
        type: str
        env:
            - name: GIT_PASSWORD
        required: no
    repo:
        description:
            - Name of the GitHub repository
            - If not set, the value of the B(GIT_REPO) environment variable is used.
        type: str
        env:
            - name: GIT_REPO
        required: yes
    org:
        description:
            - Name of the GitHub organization (or user account)
            - If not set, the value of the B(GIT_ORG) environment variable is used.
        type: str
        env:
            - name: GIT_ORG
        required: yes
    branch:
        description:
            - Name of the GitHub repository branch
        type: str
        default: master
        required: yes
    working_dir:
        description: Path to the working directory for git clone
        required: true
        type: str
'''
