#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   employee.py
@Time    :   2021/07/03 08:22:51
@Author  :   JayZhang 
@Version :   1.0
@Contact :   597952291@qq.com
@License :   (C)Copyright 2021, Liugroup-NLPR-CASIA
@Desc    :   None
'''

# here put the import lib
import requests
import time
from settings.config import settings
from sanic.response import json
import json as js
from ..util import tool

# here put the main code
BASE_URL = "https://qyapi.weixin.qq.com/cgi-bin/"
COMMON_SECRET = settings.WE_WORK_APP_SECRET['Checkin'][0]
COMMON_APPID = settings.WE_WORK_APP_SECRET['Checkin'][1]


async def get_all_department_id() -> dict:
    """获取全部部门id"""
    c = tool.CorpApp(COMMON_SECRET, COMMON_APPID)
    res = requests.get(
        BASE_URL + 'department/list?access_token={}'.format(c.access_token))
    data = js.loads(res.content.decode('utf-8'))
    [i["id"] for i in data["department"]]
    return data


async def get_all_department(request) -> any:
    """
    获取全部部门
    :param:request
    :return:any
    """
    c = tool.CorpApp(COMMON_SECRET, COMMON_APPID)
    print(c.access_token)
    res = requests.get(
        BASE_URL + 'department/list?access_token={}'.format(c.access_token))
    data = js.loads(res.content.decode('utf-8'))
    if data['errcode'] == 0 and data['errmsg'] == "ok":
        return json(data)
    else:
        return json(data)
