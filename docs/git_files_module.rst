.. Document meta

:orphan:

.. Anchors

.. _ansible_collections.techbeck03.git_controls.git_files_module:

.. Anchors: short name for ansible.builtin

.. Anchors: aliases



.. Title

techbeck03.git_controls.git_files -- Add, remove and commit files to existing git repo
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. Collection note

.. note::
    This plugin is part of the `techbeck03.git_controls collection <https://galaxy.ansible.com/techbeck03/git_controls>`_ (version 1.0.6).

    To install it use: :code:`ansible-galaxy collection install techbeck03.git_controls`.

    To use it in a playbook, specify: :code:`techbeck03.git_controls.git_files`.

.. version_added

.. versionadded:: 1.0.0 of techbeck03.git_controls

.. contents::
   :local:
   :depth: 1

.. Deprecated


Synopsis
--------

.. Description

- This module adds, removes and commits files to a git repo clone to the specified working directory


.. Aliases


.. Requirements


.. Options

Parameters
----------

.. raw:: html

    <table  border=0 cellpadding=0 class="documentation-table">
        <tr>
            <th colspan="1">Parameter</th>
            <th>Choices/<font color="blue">Defaults</font></th>
                        <th width="100%">Comments</th>
        </tr>
                    <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-add_files"></div>
                    <b>add_files</b>
                    <a class="ansibleOptionLink" href="#parameter-add_files" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=string</span>                                            </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>A list of filenames to be added to the specified git repo working directory</div>
                                            <div>Filenames can be relative to the working directory</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-branch"></div>
                    <b>branch</b>
                    <a class="ansibleOptionLink" href="#parameter-branch" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">"master"</div>
                                    </td>
                                                                <td>
                                            <div>Name of the GitHub repository branch</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-commit_string"></div>
                    <b>commit_string</b>
                    <a class="ansibleOptionLink" href="#parameter-commit_string" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The commit string used for git repo commit</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-git_password"></div>
                    <b>git_password</b>
                    <a class="ansibleOptionLink" href="#parameter-git_password" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Password used for Github authorization</div>
                                            <div>Required if <em>git_token=None</em></div>
                                            <div>If not set, the value of the <code>GIT_PASSWORD</code> environment variable is used.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-git_token"></div>
                    <b>git_token</b>
                    <a class="ansibleOptionLink" href="#parameter-git_token" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Git token used for authentication</div>
                                            <div>Required if <em>git_username=None</em></div>
                                            <div>If not set, the value of the <code>GIT_TOKEN</code> environment variable is used.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-git_username"></div>
                    <b>git_username</b>
                    <a class="ansibleOptionLink" href="#parameter-git_username" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Username used for Github authorization</div>
                                            <div>Required if <em>git_token=None</em></div>
                                            <div>If not set, the value of the <code>GIT_USERNAME</code> environment variable is used.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-org"></div>
                    <b>org</b>
                    <a class="ansibleOptionLink" href="#parameter-org" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Name of the GitHub organization (or user account)</div>
                                            <div>If not set, the value of the <code>GIT_ORG</code> environment variable is used.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-remove_files"></div>
                    <b>remove_files</b>
                    <a class="ansibleOptionLink" href="#parameter-remove_files" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=string</span>                                            </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>A list of filenames to be removed from the specified git repo working directory</div>
                                            <div>Filenames can be relative to the working directory</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-repo"></div>
                    <b>repo</b>
                    <a class="ansibleOptionLink" href="#parameter-repo" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Name of the GitHub repository</div>
                                            <div>If not set, the value of the <code>GIT_REPO</code> environment variable is used.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-working_dir"></div>
                    <b>working_dir</b>
                    <a class="ansibleOptionLink" href="#parameter-working_dir" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Path to the working directory for git clone</div>
                                                        </td>
            </tr>
                        </table>
    <br/>

.. Notes


.. Seealso


.. Examples

Examples
--------

.. code-block:: yaml+jinja

    
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





.. Facts


.. Return values

Return Values
-------------

.. raw:: html

    <table border=0 cellpadding=0 class="documentation-table">
        <tr>
            <th colspan="1">Key</th>
            <th>Returned</th>
            <th width="100%">Description</th>
        </tr>
                    <tr>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-added_files"></div>
                    <b>added_files</b>
                    <a class="ansibleOptionLink" href="#return-added_files" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">list</span>
                       / <span style="color: purple">elements=string</span>                    </div>
                                    </td>
                <td>changed</td>
                <td>
                                            <div>A list of filenames added with latest commit</div>
                                        <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">[/tmp/myrepo]</div>
                                    </td>
            </tr>
                                <tr>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-removed_files"></div>
                    <b>removed_files</b>
                    <a class="ansibleOptionLink" href="#return-removed_files" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">list</span>
                       / <span style="color: purple">elements=string</span>                    </div>
                                    </td>
                <td>changed</td>
                <td>
                                            <div>A list of filenames removed with latest commit</div>
                                        <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">[/tmp/myrepo]</div>
                                    </td>
            </tr>
                        </table>
    <br/><br/>

..  Status (Presently only deprecated)


.. Authors

Authors
~~~~~~~

- Brandon Beck (@techBeck03)



.. Parsing errors

