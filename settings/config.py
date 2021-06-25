#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    @File        :config
    @Description :
    @DateTiem    :2021/4/9 16:10
    @Author      :Jay Zhang
"""
import os

# 获取环境变量
env = os.getenv("ENV", "")
if env:
    # 如果有虚拟环境 则是且为POR 并存在生产配置对应文件-> 生产环境
    if env == 'POR' and os.path.exists('settings/settings_por.py'):
        print("----------生产环境启动------------")
        from .settings_por import settings
    else:
        # 不为POR则-> 开发环境
        print("----------开发环境启动------------")
        from .settings_dev import settings
else:
    # 没有则-> 开发环境
    print("----------开发环境启动------------")
    from .settings_dev import settings
