# -*- coding: utf-8 -*-
"""

@date 2018/5/30
@author: David Dai
================

"""


def rate_list(n):
    a = 1.0 * n / (n - 1) / (n - 1)
    data = list(map(lambda x: a * x * x + n, range(n)))
    rate = list(map(lambda x: x / sum(data), data))
    rate_reverse = rate.copy()
    rate_reverse.reverse()
    rate.extend(rate_reverse)
    return rate
