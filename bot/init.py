#!/usr/bin/env python3
import yaml
import os
from subprocess import call

config_yaml = 'repos.yaml'
repos = yaml.load(open(config_yaml))
print("load", config_yaml, "finished")

root_dir = os.path.abspath(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
git_dir = os.path.join(root_dir, "git")
os.chdir(git_dir)
print("cd into", git_dir)

max_len = max([len(x["name"]) for x in repos])
for repo in repos:
    repo_dir = os.path.join(git_dir, repo["name"])
    os.makedirs(repo_dir, exist_ok=False)
    os.chdir(repo_dir)
    call(["git", "init", "--bare"])
    call(["git", "remote", "add", "github", repo["url"]])
    call(["git", "fetch", "github"])
    print ("init repo:", "{0:>{width}}".format(repo["name"], width=max_len), "in", repo_dir, "finished")
