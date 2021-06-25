#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    @File        :database
    @Description :
    @DateTiem    :2021/3/8 12:37
    @Author      :Jay Zhang
"""
from redis import StrictRedis, ConnectionPool

from settings.config import settings


REDIS_URL = settings.CELERY_COON


# redis 连接
pool = ConnectionPool.from_url(REDIS_URL, decode_responses=True)
redis = StrictRedis(connection_pool=pool)
