#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   attendance.py
@Time    :   2021/07/03 14:14:08
@Author  :   JayZhang 
@Version :   1.0
@Contact :   597952291@qq.com
@License :   (C)Copyright 2021, Liugroup-NLPR-CASIA
@Desc    :   获取企业微信的打卡记录；每隔10分钟获取前15分钟的数据
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

# @bp.route("/get_all_user",methods=["GET"])


async def get_all_user(request):
    print(request)
    c = tool.CorpApp(COMMON_SECRET, COMMON_APPID)
    print(c.access_token)
    return json({"token": c.access_token})


async def get_all_attendance(request):
    """获取全部考勤记录"""
    print(request)
    user_list = ["hp0786", "hp0789"]
    print("userList", user_list)
    c = tool.CorpApp(COMMON_SECRET, COMMON_APPID)
    access_token = c.access_token
    print("c.access_token", access_token)
    print("starttime", int(time.time())-(86400*5)) # 86400为一天的时间戳秒数
    print("endtime", int(time.time()))
    res = requests.post(BASE_URL + 'checkin/getcheckindata?access_token={}'.format(access_token),
                        js.dumps({
                            "opencheckindatatype": 3,
                            "starttime": int(time.time())-(86400*5),
                            "endtime": int(time.time()),
                            "useridlist": user_list
                        })
                        )
    data = js.loads(res.content.decode('utf-8'))
    if data['errcode'] == 0 and data['errmsg'] == "ok":
        return json(data['checkindata'])
    else:
        return json(data)
