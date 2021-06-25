#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    @File        :settings_dev
    @Description :
    @DateTiem    :2021/4/9 15:52
    @Author      :Jay Zhang
"""


class Settings:
    # SAP_URL = 'http://116.62.212.230:8089/'  # SAP接口地址
    # SAP_CARD_CODE = "108000076"  # SAP销售订单同样客户编码
    CELERY_COON = 'redis://:redis123!@localhost:6379/6'  # redis 地址

    SP_URL = "https://uat-sockpress-middleware.getconnectplus.com"

    DATABASE = {
        'we_chat_app': 'mysql://root:root@localhost/admin?charset=utf8',
        'oms': 'mysql://root:root@127.0.0.1/fs_oms?charset=utf8mb4',
        'tiny': 'mysql://root:root@127.0.0.1/tiny?charset=utf8mb4',
        # 'sap': 'mssql+pyodbc://sa:Zy2017@116.62.212.230:1433/ZY_NEW_TEST?driver=ODBC+Driver+13+for+Sql+Server',
        'warehouse': 'mysql://root:root@127.0.0.1/fs_warehouse?charset=utf8mb4'
    }
    WE_WORK_CORP_ID = 'wx5823bf96d3bd56c7'  # 企业微信公司id
    WE_WORK_APP_SECRET = {  # 企业微信内部应用密钥,id
        'oms': ['MAyNmD6rqas9sTzVOUFP4Na4nV0XivmVqp-czMIVo_c', '1000031']
    }


# 实例化配置对象
settings = Settings()
