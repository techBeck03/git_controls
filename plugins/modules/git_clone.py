#!/usr/bin/python

# Copyright: (c) 2018, Terry Jones <terry.jones@example.org>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r'''
---
module: git_clone

short_description: Add or remove a local git repo clone

version_added: "1.0.0"

description: This module adds or removes a git repo clone to the specified working directory

options:
    state:
        description:
            - If I(state=present) the specified repo will be cloned to the working directory
            - If I(state=absent) the specified working directory will be removed
        required: false
        type: str
        default: present
        choices:
            - present
            - absent
    auto_generate_parent:
        description:
            - If C(True) a unique folder will be created in the provided working directory
            - to house the cloned repo
        required: false
        type: str
        default: False
    pull:
        description:
            - If C(True) a git pull is executed if I(working_dir) contains an existing git repo
        required: false
        type: str
        default: False
extends_documentation_fragment:
    - git
author:
    - Brandon Beck (@techBeck03)
'''

EXAMPLES = r'''
# Clone git repo to auto-generated folder
-   name: Clone git repo to auto-generated folder
    techbeck03.git_controls.git_clone.git_clone:
        repo: "myrepo"
        org: "username"
        branch: "master"
        auto_generate_parent: True
        working_dir: /tmp
        state: present

# Clone a repo
-   name: Clone git repo to existing folder and pull latest changes
    techbeck03.git_controls.git_clone.git_clone:
        repo: "myrepo"
        org: "username"
        branch: "master"
        pull: True
        working_dir: /tmp/myrepo
        state: present

'''

RETURN = r'''
# These are examples of possible return values, and in general should use other names for return values.
working_dir:
    description: The path to working directory for the cloned git repo
    type: str
    returned: always
    sample: '/tmp/myrepo'
'''

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.git import GitModule, git_argument_spec

def run_module():
    # define available arguments/parameters a user can pass to the module
    module_args = dict(
        working_dir=dict(type='str', required=True),
        auto_generate_parent=dict(type='bool', default=False),
        pull=dict(type='bool', default=False),
        state=dict(type='str', default="present", choices=['present', 'absent']),
    )
    module_args.update(git_argument_spec)

    result = dict(
        changed=False,
        working_dir=None
    )
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=False,
        mutually_exclusive=[('auto_generate_parent', 'pull')]
    )
    git = GitModule(module)
    state = module.params.get("state")
    auto_generate_parent = module.params.get("auto_generate_parent")
    pull = module.params.get("pull")

    if state == "present":
        clone_result = git.cloneRepo(auto_generate_parent=auto_generate_parent, pull=pull)
        result['changed'] = True if clone_result['status'] == 'modified' else False
        result['working_dir'] = clone_result['working_dir']
    elif state == "absent":
        result["changed"] = git.removeRepo()
    module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()