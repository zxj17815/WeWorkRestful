#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   call_back.py
@Time    :   2021/06/25 10:21:26
@Author  :   JayZhang 
@Version :   1.0
@Contact :   597952291@qq.com
@License :   (C)Copyright 2021, Liugroup-NLPR-CASIA
@Desc    :   None
'''

# here put the import lib
from sanic.response import json
from ..util import tool
import xml.etree.ElementTree as ET

# here put the main code


async def call_back_get(request):
    print(request)
    data = request.GET.dict()
    return json(tool.call_back_verify(data, 'sap'))


async def call_back_post(request):
    url_data = {
        "msg_signature": request.args.get("msg_signature"),
        "timestamp": request.args.get("timestamp"),
        "nonce": request.args.get("nonce"),
    }
    print(url_data)
    print('body', request.body.decode("utf-8"))
    cb = tool.call_back_data(
        url_data, request.body.decode("utf-8"))
    return json(cb, content_type="application/json")
