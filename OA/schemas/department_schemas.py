#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   department.py
@Time    :   2021/07/05 15:37:07
@Author  :   JayZhang 
@Version :   1.0
@Contact :   597952291@qq.com
@License :   (C)Copyright 2021, iceiceice
@Desc    :   None
'''

# here put the import lib
from pydantic import BaseModel
from datetime import datetime

# here put the main code


class HrmDepartmentBase(BaseModel):
    """部门"""
    id: int = None
    departmentname: str = None

    class Config:
        orm_mode = True


class HrmDepartment(BaseModel):
    """部门"""
    id: int = None
    cid: int = None
    subcompanyname: str = None
    pid: int = None
    departmentname: str = None

    class Config:
        orm_mode = True
