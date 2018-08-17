# -*- coding: utf-8 -*-
"""

@date 2018/4/11
@author: Dai Wei
================

"""
import inspect
import os
from functools import wraps

import numpy as np
import pandas as pd
from scipy.sparse import coo_matrix
from sklearn import preprocessing

import log
from .config import get_config
from .str import md5


def random_dataframe(data):
    reindex = data.index.values.copy()
    np.random.shuffle(reindex)
    return data.ix[reindex, :]


def astype_map(data, type_map):
    for k, v in type_map.items():
        data[k] = data[k].astype(v)


def astype_list(data, type_list):
    type_map = {}
    for column, v in zip(data.columns.values, type_list):
        type_map[column] = v
    astype_map(data, type_map)


def generate_data(columns=['key1', 'key2', 'key3', 'key4'], size=(4, 4)):
    data = np.random.random_integers(0, 10, size)
    return pd.DataFrame(np.array(data), columns=columns)


def save(data, file_name='data'):
    np.savez(file_name, data=data.values, index=data.index, columns=data.columns, dtype=data.dtypes)


def load(file_name='data'):
    data = np.load(file_name + '.npz')
    ret = pd.DataFrame(data['data'], index=data['index'], columns=data['columns'])
    astype_list(ret, data['dtype'])
    return ret


def max_min_preprocess(data, columns):
    prepcocess_data = data[columns]
    z_data = preprocessing.MinMaxScaler().fit_transform(prepcocess_data.values)
    return pd.DataFrame(z_data, index=prepcocess_data.index, columns=columns) \
        .join(data[filter(lambda x: x not in columns, data.columns)])


def to_dict(data, columns, target):
    ret = {}
    if len(columns) == 1:
        return data.set_index(columns[0])[target].to_dict()
    for item, group in data.groupby(columns[0]):
        temp_columns = columns[1:]
        temp_columns.append(target)
        ret[item] = to_dict(group[temp_columns], columns[1:], target)
    return ret


def type_format(arg):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kw):
            type_map = {}
            res = func(*args, **kw)
            if not isinstance(res, pd.DataFrame):
                raise TypeError('is not pd.DataFrame')
            if isinstance(arg, list):
                for column, v in zip(res.columns.values, arg):
                    type_map[column] = v
            if isinstance(arg, dict):
                type_map = arg
            astype_map(res, type_map)
            return res

        return wrapper

    return decorator


def cache_pd(func):
    @wraps(func)
    def wrapper(*args, **kv):
        # get cache path
        cache_path = get_config('cache_path', 'path')
        if not os.path.exists(cache_path):
            os.makedirs(cache_path)
        # get file name
        lines = inspect.getsourcelines(func)
        code = "".join(lines[0])
        if code.find('self'):
            code = code + str(args[1:]) + str(kv)
        else:
            code = str(args) + str(kv)
        file_name = cache_path + '/' + md5(code)
        if os.path.exists(file_name + '.npz'):
            return load(file_name)
        res = func(*args, **kv)
        if not isinstance(res, pd.DataFrame):
            raise TypeError('is not pd.DataFrame')
        save(res, file_name)
        log.info('cache the pd.DataFrame, save to %s' % file_name)
        return res

    return wrapper


def to_coo_matrix(data, x_column, y_column, value_column):
    """to item user matrix"""
    n, m = data[y_column].drop_duplicates().count(), data[x_column].drop_duplicates().count()
    data_values = data[[y_column, x_column, value_column]].values
    return coo_matrix((data_values[:, 2], (data_values[:, 1], data_values[:, 0])), shape=(m, n))


def coo_matrix_to_pd(matrix, x_column, y_column, values_column):
    data = pd.DataFrame()
    data[y_column] = matrix.col
    data[x_column] = matrix.row
    data[values_column] = matrix.data
    return data
