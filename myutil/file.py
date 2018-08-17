# -*- coding: utf-8 -*-
"""

@date 2018/4/12
@author: David Dai
================

"""

import json
import os
import subprocess


def get_lines_num_wc(file_path):
    ret = subprocess.getoutput('wc -l %s' % file_path)
    return int(ret.strip().split(' ')[0])


def get_lines_num_io(file_path):
    count = 0
    for count, line in enumerate(open(file_path, 'r')):
        pass
    count += 1
    return count


def check_file(file_path: str):
    """check file exit"""
    return os.path.isfile(file_path)


def check_dir(path: str) -> bool:
    """check path is dir, if not create it"""
    if not os.path.isdir(path):
        os.mkdir(path)
        return False
    return True


def remove_files(path: str):
    """remove all file in the path"""
    if len(os.listdir(path)) > 0:
        subprocess.check_call("rm -r %s/*" % path, shell=True)


def load_json_file(path: str) -> dict:
    json_path = path
    with open(json_path, 'r') as f:
        return json.load(f)


def jump_json_file(data: dict, path: str):
    with open(path, 'w') as f:
        json.dump(data, f)


def remove_files_list(files_list: list):
    for file in files_list:
        remove_file(file)


def remove_file(file_path: str):
    if os.path.isfile(file_path):
        os.remove(file_path)
        return True
    else:
        return False


if __name__ == '__main__':
    path = "/Users/daiwei/workspace/nlp/resources/punc/output/v1"
    remove_file(path + '/weights.epoch1.hdf5')
