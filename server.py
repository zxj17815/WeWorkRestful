#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   server.py
@Time    :   2021/06/17 15:50:17
@Author  :   JayZhang 
@Version :   1.0
@Contact :   597952291@qq.com
@License :   (C)Copyright 2021, Liugroup-NLPR-CASIA
@Desc    :   启动文件
'''

# here put the import lib
from main import app
import multiprocessing


# here put the main code
workers = multiprocessing.cpu_count()
print("cpu count:{} starting...".format(workers))
app.run(host='0.0.0.0', port=8000, workers=workers)
