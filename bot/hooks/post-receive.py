#!/usr/bin/env python3

from sys import argv
import os
from subprocess import call

git_dir = os.getcwd()
hook_dir = os.path.abspath(os.path.dirname(os.path.realpath(__file__)))

print(git_dir)
print(hook_dir)

