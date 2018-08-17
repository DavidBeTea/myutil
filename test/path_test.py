# -*- coding: utf-8 -*-
"""
Path
@date 2018/4/9
@author: David Dai
================

"""

import unittest
import numpy as np
import pandas as pd

from utils.path import get_project_path


class PathTest(unittest.TestCase):
    def test(self):
        pass

    def test_get_project_path(self):
        data = get_project_path()
        print(data)

    def setUp(self):
        pass

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
