#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    @File        :settings_dev
    @Description :
    @DateTiem    :2021/4/9 15:52
    @Author      :Jay Zhang
"""


class Settings:
    # SAP_URL = ''  # SAP接口地址
    CELERY_COON = 'redis://:redis123!@localhost:6379/6'  # redis 地址

    DATABASE = {
        'we_chat_app': 'mysql://root:root@localhost/admin?charset=utf8',
        'tiny': 'mysql://root:root@127.0.0.1/tiny?charset=utf8mb4',
        # 'sap': 'mssql+pyodbc://sa:Zy2017@116.62.212.231:1433/NEW_TEST?driver=ODBC+Driver+13+for+Sql+Server',
    }
    WE_WORK_CORP_ID = 'ww2dc8f6e94a910ffe'  # 企业微信公司id
    WE_WORK_URL = 'https://qyapi.weixin.qq.com/cgi-bin/'  # 企业微信URL
    WE_WORK_APP_SECRET = {  # 企业微信内部应用密钥,id
        'Common': ['K2bafPldkS_OcukeyaO4u4Go15odgC-vXIA5oU4jTNA', '1000011'],
        'Checkin': ['dEH28twWi8MPAwRN573pCR-Bxu26UmNcb4UzqM6814g', '3010011']
    }


# 实例化配置对象
settings = Settings()
