#!/usr/bin/env python3
# we use a seperate repo to trigger hooks, because it's hard for a repo to know
# if other repos are also being updated(in which case the last-finished repo
# should trigger the build process)

import yaml
import os
from subprocess import call

root_dir = os.path.abspath(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
hook_dir = os.path.join(root_dir, "bot", "hooks")
git_dir = os.path.join(root_dir, "git", "hooks")
os.makedirs(git_dir, exist_ok=True)
os.chdir(git_dir)
call(["git", "init", "--bare"])
os.chdir("hooks")

hooks_rel_path = os.path.relpath(hook_dir, os.getcwd())
for hook in os.listdir(hook_dir):
    print("set up hook", hook)
    call(["ln", "-sf", os.path.join(hooks_rel_path, hook), os.path.splitext(hook)[0]])

