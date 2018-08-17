# -*- coding: utf-8 -*-
"""

@date 2018/3/30
@author: David Dai
================

"""
import logging

import sys

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s:%(message)s')

g_logger = logging.getLogger()


def import_log_funcs():
    global g_logger

    curr_mod = sys.modules[__name__]
    log_funcs = ['debug', 'info', 'warning', 'error', 'critical',
                 'exception']

    for func_name in log_funcs:
        func = getattr(g_logger, func_name)
        setattr(curr_mod, func_name, func)


import_log_funcs()
