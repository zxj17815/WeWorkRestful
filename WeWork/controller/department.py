#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   department.py
@Time    :   2021/07/03 16:33:30
@Author  :   JayZhang 
@Version :   1.0
@Contact :   597952291@qq.com
@License :   (C)Copyright 2021, Liugroup-NLPR-CASIA
@Desc    :   None
'''

# here put the import lib
from xml.etree.ElementTree import Element
from xml.dom.minidom import parseString
import requests
import time
import dicttoxml
from settings.config import settings
from sanic.response import HTTPResponse, json, text
import json as js
from ..util import tool

# here put the main code
BASE_URL = "https://qyapi.weixin.qq.com/cgi-bin/"
COMMON_SECRET = settings.WE_WORK_APP_SECRET['Checkin'][0]
COMMON_APPID = settings.WE_WORK_APP_SECRET['Checkin'][1]


def dict_to_xml(tag, d):
    '''
    Turn a simple dict of key/value pairs into XML
    '''
    elem = Element(tag)
    for key, val in d.items():
        child = Element(key)
        child.text = str(val)
        elem.append(child)
    return elem


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
        data = bxml = dicttoxml.dicttoxml(
            data["department"], custom_root='bm')
        print(data)
        return HTTPResponse(data, content_type="application/xml;charset=utf-8")
    else:
        return json(data)
