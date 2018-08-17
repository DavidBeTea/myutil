# -*- coding: utf-8 -*-
"""

@date 2017/11/27
@author: Zhao Xin
================

"""
import subprocess
import time


def update_version():
    with open('setup.py', 'r') as file:
        content = str(file.read())
        start_begin = content.find('VERSION = ')
        begin = content.find("\"", start_begin)
        end = content.find("\"", begin + 1)
        version = content[begin + 1:end].split('.')
    version[2] = str(int(version[2]) + 1)
    with open('setup.py', 'w') as file:
        file.write(content[:begin + 1] + '.'.join(version) + content[end:])
    return '.'.join(version)


new_version = update_version()

git_process = ["git pull origin master",
               "git add --all",
               "git commit -m 'update new version %s' " % new_version,
               "git push origin"]
subprocess.check_call("python setup.py sdist", shell=True)
for command in git_process:
    subprocess.check_call(command, shell=True)
time.sleep(4)
subprocess.check_call("pip install git+ssh://git@github.com/DavidBeTea/myutil.git -U", shell=True)
# subprocess.check_call("pip install myutil/", shell=True)
subprocess.check_call("pip list | grep myutil", shell=True)
