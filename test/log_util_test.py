# -*- coding: utf-8 -*-
"""
LogUtil
@date 2018/5/9
@author: David Dai
================

"""

import unittest
import numpy as np
import pandas as pd
from myutil.log_util import run_time_email

import myutil.log as log


@run_time_email('dafdf@qq.com')
def run_test():
    log.info('run')
    print(1/0)


class LogUtilTest(unittest.TestCase):

    def test_run_time_email(self):
        run_test()

    def test(self):
        pass

    def setUp(self):
        pass

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
