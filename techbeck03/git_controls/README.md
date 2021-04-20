# Ansible Collection - techbeck03.git_controls

Ansible collection for doing basic tasks against a GitHub repository.

## Requirements

- Ansible v2.11 or newer (due to limited testing)
- `GitPython` (pip)
- `git` system executable

## Supported modules

- `techbeck03.git_controls.git_clone`: Clones an existing repo to a target working directory (also supports cleanup)
- `techbeck03.git_controls.git_files`: Adds, Removes and commits file changes to target git repository
