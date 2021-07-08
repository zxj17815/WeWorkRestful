#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   database.py
@Time    :   2021/07/05 13:24:13
@Author  :   JayZhang 
@Version :   1.0
@Contact :   597952291@qq.com
@License :   (C)Copyright 2021, iceiceice
@Desc    :   None
'''

# here put the import lib
from sqlalchemy import create_engine

# here put the main code

bind = create_engine(
    'mssql+pyodbc://sa:Hnhp123.@192.168.2.6/ecology?driver=ODBC+Driver+13+for+Sql+Server', encoding='utf_8', echo=True)
