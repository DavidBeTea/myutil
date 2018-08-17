# -*- coding: utf-8 -*-
"""

@date 2017/4/11
@author: Dai Wei
================

"""
import time
from datetime import datetime
from functools import wraps

import yagmail

import log
from .config import get_config


def run_time(func):
    @wraps(func)
    def wrapper(*args, **kw):
        start = time.time()
        res = func(*args, **kw)
        end = time.time()
        log.info("%s : %s second" % (func.__name__, (end - start)))
        return res

    return wrapper


def run_time_email(to):
    def decorator(func):
        address = get_config('email', 'address')
        password = get_config('email', 'password')
        me = 'david.dai@zoom.us'
        explain = "<p align='right'> This is send by python</p>"
        sign = "<p align='right'> David Dai || Zoom </p>"

        @wraps(func)
        def wrapper(*args, **kw):
            start = time.time()
            try:
                res = func(*args, **kw)
                exception_error = ''
            except Exception as e:
                exception_error = 'catch Exception : \n %s' % e
            finally:
                yag = yagmail.SMTP(user=address, password=password, port='25', smtp_ssl=False)
                end = time.time()
                content = func.__code__.co_filename + ' ' + func.__name__ + ' run time ：' + str(end - start)
                yag.send(to, func.__name__ + ' Running Log', [res.__str__(), content, explain, sign, exception_error], cc=me)
                log.info(func.__name__ + ' running time : ' + str(end - start))
                if exception_error:
                    log.info('%s Run failed, Error Mes:%s' % (func.__name__, exception_error))
                return res

        return wrapper

    return decorator


def log_email(to):
    def decorator(func):
        address = get_config('email', 'address')
        password = get_config('email', 'password')
        log_file = get_config('log_path', 'path')
        ssl_check = True if get_config('pub_mail', 'ssl_check') else False
        if ssl_check:
            yag = yagmail.SMTP(user=address, password=password, port='25', smtp_ssl=False)
        else:
            yag = yagmail.SMTP(user=address, password=password, port='25')

        @wraps(func)
        def wrapper(*args, **kv):
            output = open(log_file, 'a')
            begin_flag = 'LOG EMAIL BEGIN ' + datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            output.write(begin_flag)
            output.close()
            ret = func(*args, **kv)
            output = open(log_file, 'r')
            logs = output.read()
            output.close()
            begin = logs.find(begin_flag)
            content = logs[begin:]
            yag.send(to, func.func_name + ' log Email', [content])
            return ret

        return wrapper

    return decorator


def email_content(content: str, to: str, topic=None):
    address = get_config('email', 'address')
    password = get_config('email', 'password')
    me = 'david.dai@zoom.us'
    explain = "<p align='right'> This is send by python</p>"
    sign = "<p align='right'> David Dai || Zoom </p>"
    yag = yagmail.SMTP(user=address, password=password, port='25', smtp_ssl=False)
    topic = topic if topic else "AUTO Eamil INFO"
    yag.send(to, topic, [content, explain, sign], cc=me)
