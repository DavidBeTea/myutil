# -*- coding: utf-8 -*-
"""

@date 2018/4/9
@author: David Dai
================

"""
import os
import sys


def get_project_path(file='README.md'):
    path_argv, filename = os.path.split(os.path.abspath(sys.argv[0]))
    paths = [path_argv, os.getcwd()]
    if os.path.isfile(path_argv+'/'+file):
        return path_argv
    for path in paths:
        path_split = path.split('/')
        for i in range(1, len(path_split)):
            check_path = '/'.join(path_split[:-i])
            if os.path.isfile(check_path + '/' + file):
                return check_path


if __name__ == '__main__':
    print(get_project_path())
