#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   model.py
@Time    :   2021/06/23 16:01:26
@Author  :   JayZhang 
@Version :   1.0
@Contact :   597952291@qq.com
@License :   (C)Copyright 2021, iceiceice
@Desc    :   数据模型
'''

# here put the import lib
from sqlalchemy import INTEGER, Column, ForeignKey, String
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

# here put the main code


class HrmDepartment(Base):
    """部门"""
    __tablename__ = 'HrmDepartment'

    id = Column(INTEGER(), primary_key=True)
    departmentname = Column(String())
    supdepid = Column(INTEGER())
    subcompanyid1 = Column(INTEGER())


class HrmSubCompany(Base):
    """公司"""
    __tablename__ = 'HrmSubCompany'

    id = Column(INTEGER(), primary_key=True)
    subcompanyname = Column(String())
