.. Document meta

:orphan:

.. Anchors

.. _ansible_collections.techbeck03.git_controls.git_clone_module:

.. Anchors: short name for ansible.builtin

.. Anchors: aliases



.. Title

techbeck03.git_controls.git_clone -- Add or remove a local git repo clone
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. Collection note

.. note::
    This plugin is part of the `techbeck03.git_controls collection <https://galaxy.ansible.com/techbeck03/git_controls>`_ (version 1.0.6).

    To install it use: :code:`ansible-galaxy collection install techbeck03.git_controls`.

    To use it in a playbook, specify: :code:`techbeck03.git_controls.git_clone`.

.. version_added

.. versionadded:: 1.0.0 of techbeck03.git_controls

.. contents::
   :local:
   :depth: 1

.. Deprecated


Synopsis
--------

.. Description

- This module adds or removes a git repo clone to the specified working directory


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
                    <div class="ansibleOptionAnchor" id="parameter-auto_generate_parent"></div>
                    <b>auto_generate_parent</b>
                    <a class="ansibleOptionLink" href="#parameter-auto_generate_parent" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                                                                                <b>Default:</b><br/><div style="color: blue">"no"</div>
                                    </td>
                                                                <td>
                                            <div>If <code>True</code> a unique folder will be created in the provided working directory</div>
                                            <div>to house the cloned repo</div>
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
                    <div class="ansibleOptionAnchor" id="parameter-pull"></div>
                    <b>pull</b>
                    <a class="ansibleOptionLink" href="#parameter-pull" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                                                                                <b>Default:</b><br/><div style="color: blue">"no"</div>
                                    </td>
                                                                <td>
                                            <div>If <code>True</code> a git pull is executed if <em>working_dir</em> contains an existing git repo</div>
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
                    <div class="ansibleOptionAnchor" id="parameter-state"></div>
                    <b>state</b>
                    <a class="ansibleOptionLink" href="#parameter-state" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li><div style="color: blue"><b>present</b>&nbsp;&larr;</div></li>
                                                                                                                                                                                                <li>absent</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>If <em>state=present</em> the specified repo will be cloned to the working directory</div>
                                            <div>If <em>state=absent</em> the specified working directory will be removed</div>
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





.. Facts


.. Return values

Return Values
-------------
Common return values are documented :ref:`here <common_return_values>`, the following are the fields unique to this module:

.. raw:: html

    <table border=0 cellpadding=0 class="documentation-table">
        <tr>
            <th colspan="1">Key</th>
            <th>Returned</th>
            <th width="100%">Description</th>
        </tr>
                    <tr>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-working_dir"></div>
                    <b>working_dir</b>
                    <a class="ansibleOptionLink" href="#return-working_dir" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>always</td>
                <td>
                                            <div>The path to working directory for the cloned git repo</div>
                                        <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">/tmp/myrepo</div>
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

