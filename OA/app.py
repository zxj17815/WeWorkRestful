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
from .controller import dataform


# here put the main code
# ./my_blueprint.py


bp = Blueprint("oa", url_prefix="oa")


bp.add_route(
    dataform.get_department,
    '/get_department',
    methods=["get"],
)
