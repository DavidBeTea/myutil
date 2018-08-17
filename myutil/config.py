# -*- coding: utf-8 -*-
"""

@date 2018/4/9
@author: David Dai
================

"""
from configparser import ConfigParser

import log
from .path import get_project_path


def get_config(key1, key2, config_path=None):
    if not config_path:
        config_path = get_project_path() + '/config'
    config = ConfigParser()
    config.read(config_path)
    try:
        return config.get(key1, key2)
    except Exception:
        log.info("config path not finde ,default file is %s" % config_path)
