#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   main.py
@Time    :   2021/06/17 15:23:43
@Author  :   JayZhang 
@Version :   1.0
@Contact :   597952291@qq.com
@License :   (C)Copyright 2021, iceiceice
@Desc    :   None
'''

# here put the import lib
import asyncio

from sanic import Sanic
from helper import HttpResponse
from sanic_openapi import swagger_blueprint
from WeWork.app import bp as we_work_bp
from OA.app import bp as oa_bp
from contextvars import ContextVar

# from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import sessionmaker
from OA.database import bind


# here put the main code
app = Sanic("WeWorkRestful")

app.blueprint(swagger_blueprint)

app.blueprint(we_work_bp)

app.blueprint(oa_bp)

print("app mode: {}".format(app.config.MODE))


@app.get("/test")
async def hello_world(request):
    # print(request.ctx.user)
    return HttpResponse.ok({"say": "Hello, world."})


_base_model_session_ctx = ContextVar("session")


@app.middleware("request")
async def inject_session(request):
    request.ctx.session = sessionmaker(bind)()
    request.ctx.session_ctx_token = _base_model_session_ctx.set(
        request.ctx.session)


@app.middleware("response")
async def close_session(request, response):
    if hasattr(request.ctx, "session_ctx_token"):
        _base_model_session_ctx.reset(request.ctx.session_ctx_token)
        request.ctx.session.close()

# async def notify_server_started_after_five_seconds(t):
#     await asyncio.sleep(t)
#     print('Server successfully started! -{}'.format(t))

# app.add_task(notify_server_started_after_five_seconds(5))
# app.add_task(notify_server_started_after_five_seconds(10))

# @app.middleware("request")
# async def extract_user(request):
#     print("request_middleware:{}".format(request.ctx))
#     request.ctx.user = "testUser"
#     # return HttpResponse.param_error({"say": "bye, world."})


# @app.middleware('response')
# async def prevent_xss(request, response):
#     print("response_middleware:{}".format(response.body))
#     response.headers["x-xss-protection"] = "1; mode=block"

# @app.listener("before_server_start")
# async def listener_1(app, loop):
#     print("before_server_start_listener_1")


# @app.listener("before_server_start")
# async def listener_2(app, loop):
#     print("before_server_start_listener_2")


# @app.listener("after_server_start")
# async def listener_3(app, loop):
#     print("after_server_start_listener_3")


# @app.listener("after_server_start")
# async def listener_4(app, loop):
#     print("after_server_start_listener_4")


# @app.listener("before_server_stop")
# async def listener_5(app, loop):
#     print("listener_5")


# @app.listener("before_server_stop")
# async def listener_6(app, loop):
#     print("listener_6")


# @app.listener("after_server_stop")
# async def listener_7(app, loop):
#     print("listener_7")


# @app.listener("after_server_stop")
# async def listener_8(app, loop):
#     print("listener_8")
