#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   HttpResponse.py
@Time    :   2021/06/22 09:32:49
@Author  :   JayZhang 
@Version :   1.0
@Contact :   597952291@qq.com
@License :   (C)Copyright 2021, Liugroup-NLPR-CASIA
@Desc    :   None
'''

# here put the import lib
from sanic.response import HTTPResponse, json, text
from .ErrorCode import *

# here put the main code


def ok(data: dict) -> HTTPResponse:
    """
    Return 200 status HTTPResponse
    :param:code:int
    :param:data:dict
    :return:HTTPResponse
    """
    res = {
        "errcode": OK,
        "data": data
    }
    return json(res, 200)


def param_error(error_fields: dict[str, str]) -> HTTPResponse:
    """
    Return 400 param error
    :param:error_fields:dict[str,str] 
    :param:errcode:int
    :return:HTTPResponse
    """
    res = {
        "errcode": RequestError.param.value,
        "data": error_fields
    }
    return json(res, 400)


def auth_error(msg: str = "auth error") -> HTTPResponse:
    """
    Return 401 auth error
    :param:error_fields:dict[str,str] 
    :param:errcode:int
    :return:HTTPResponse
    """
    res = {
        "errcode": RequestError.auth.value,
        "data": msg
    }
    return json(res, 401)


def permission_error(msg: str = "no permission") -> HTTPResponse:
    """
    Return 403 permission error
    :param:error_fields:dict[str,str] 
    :param:errcode:int
    :return:HTTPResponse
    """
    res = {
        "errcode": RequestError.permission.value,
        "data": msg
    }
    return json(res, 403)
