#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   main.py
@Time    :   2021/06/17 15:23:43
@Author  :   JayZhang 
@Version :   1.0
@Contact :   597952291@qq.com
@License :   (C)Copyright 2021, MIT
@Desc    :   None
'''

# here put the import lib
from sanic import Sanic
from sanic.response import text


# here put the main code
app = Sanic("WeWorkRestful")


@app.get("/")
async def hello_world(request):
    print(request)
    return text("Hello, world.")
