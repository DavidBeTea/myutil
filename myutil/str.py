# -*- coding: utf-8 -*-
"""

@date 2018/04/10
@author: David Dai
================

"""


def md5(s):
    import hashlib
    import types
    if type(s) is types.StringType:
        m = hashlib.md5()
        m.update(s)
        return m.hexdigest()
    else:
        return ''
