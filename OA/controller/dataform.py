#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   dataform.py
@Time    :   2021/07/05 13:12:33
@Author  :   JayZhang 
@Version :   1.0
@Contact :   597952291@qq.com
@License :   (C)Copyright 2021, iceiceice
@Desc    :   None
'''

# here put the import lib

import dicttoxml
from sanic.response import HTTPResponse, json
from sqlalchemy import select, text
import requests
from sqlalchemy.orm.session import Session
from .. import model
from ..schemas import department_schemas
from ..database import bind
# here put the main code


async def get_department(request):
    session: Session = request.ctx.session
    with session.begin():
        # data = session.query(model.HrmDepartment).first()
        # department = department_schemas.HrmDepartmentBase.from_orm(data)

        data = session.query(model.HrmDepartment.id, model.HrmDepartment.departmentname, model.HrmDepartment.supdepid.label('pid'), model.HrmSubCompany.id.label("cid"), model.HrmSubCompany.subcompanyname).join(
            model.HrmSubCompany, model.HrmSubCompany.id == model.HrmDepartment.subcompanyid1).all()
        print('data', data)

        departments = [department_schemas.HrmDepartment.from_orm(
            item).dict() for item in data]
        # try:
        #     data = session.execute(
        #         "SELECT a.id , b.supsubcomid AS cid, b.subcompanyname, a.supdepid AS pid, a.departmentname FROM HrmDepartment a INNER JOIN HrmSubCompany b ON a.subcompanyid1=b.id")
        #     rows = data.fetchall()
        #     for item in rows:
        #         print(item)
        #     print("rowcount", data.rowcount)
        #     department = department_schemas.HrmDepartment.from_orm(rows)
        # except Exception as e:
        #     print(e)
    print("departments", departments)
    # return json(departments)
    data_xml = dicttoxml.dicttoxml(
        departments, custom_root='bm')
    print(data_xml)
    return HTTPResponse(data_xml, content_type="application/xml;charset=utf-8")
