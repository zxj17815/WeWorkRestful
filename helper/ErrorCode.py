#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   ErrorCode.py
@Time    :   2021/06/22 10:17:34
@Author  :   JayZhang 
@Version :   1.0
@Contact :   597952291@qq.com
@License :   (C)Copyright 2021, Liugroup-NLPR-CASIA
@Desc    :   None
'''

# here put the import lib
from enum import Enum


# here put the main code


OK = 0  # no error


class SysError(Enum):
    """python's(system) error start 1000~1999 语法级系统级错误
    """
    other = 1000


class AppError(Enum):
    """app's error start 2000~2999 应用级错误
    """
    other = 2000


class RequestError(Enum):
    """request error start 3000 请求错误
    """
    param = 3001,  # 请求参数错误
    auth = 3101,  # 请求auth验证错误
    permission = 3201  # 请求无权限，权限不符合
