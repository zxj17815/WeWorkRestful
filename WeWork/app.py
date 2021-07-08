#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   app.py
@Time    :   2021/06/23 16:01:58
@Author  :   JayZhang 
@Version :   1.0
@Contact :   597952291@qq.com
@License :   (C)Copyright 2021, iceiceice
@Desc    :   蓝图入口
'''

# here put the import lib
from sanic.response import json
from sanic import Blueprint
from .controller import call_back, attendance, department


# here put the main code
# ./my_blueprint.py


bp = Blueprint("we_work", url_prefix="wework")


@bp.route("/")
async def bp_root(request):
    return json({"bp": "we work"})

bp.add_route(
    call_back.call_back_get,
    '/call_back',
    methods=["get"],
)
bp.add_route(
    call_back.call_back_post,
    '/call_back',
    methods=["post"],
)


bp.add_route(
    attendance.get_all_attendance,
    '/get_all_attendance',
    methods=["get"]
)

bp.add_route(
    department.get_all_department,
    '/get_all_department',
    methods=["get"]
)
