#!/usr/bin/python
# -*- coding: UTF-8 -*-
from dal import DALC

class DevideinfoDALC(DALC):
    # 设备信息
    def __init__(self):
        super(DevideinfoDALC, self).__init__()
        self.table = "devideinfo"
        self.columns = (
            'devideName',
            'reachTime',
            'setupTime',
            'devideSN' ,
            'IP',
            'netmask',
            'warranty',
            'warrantDeadTime',
            'manufactureID',
            'manufactureName',
            'bankID',
            'bankName',
            'model',
            'batch',
            'siteId',
            'siteName',
        )


class BankinfoDALC(DALC):
    # 银行信息
    def __init__(self):
        super(BankinfoDALC, self).__init__()
        self.table = "bankinfo"
        self.columns = (
            'bankID',
            'bankName'
        )

class WordrecordDALC(DALC):
    # 文档记录
    def __init__(self):
        super(WordrecordDALC, self).__init__()
        self.table = 'wordrecord'
        self.columns = (
            'describe',
            'serviceType',
            'chargeType',
            'money',
            'servicePriority',
            'serviceDescirbe',
            'changeUnitDescribe',
            'reportTime',
            'completeTime',
            'trainDescribe',
            'otherInfo',
            'img',
            'deviceSN',
            'deviceName',
            'staffName',
            'recordID',
        )

class ContactinfoDALC(DALC):
    def __init__(self):
        super(ContactinfoDALC, self).__init__()
        self.table = 'contactinfo'
        self.columns = (
            'name',
            'contact'
        )

class DeviceunitDALC(DALC):
    def __init__(self):
        super(DeviceunitDALC, self).__init__()
        self.table = 'deviceunit'
        self.columns = (
            'deviceModel',
            'devideBatch',
            'unitModel',
            'unitName'
        )

class ModelinfoDALC(DALC):
    def __init__(self):
        super(ModelinfoDALC, self).__init__()
        self.table = 'modelinfo'
        self.columns = (
            'modelID',
            'batch'
        )

class SitecontactDALC(DALC):
    def __init__(self):
        super(SitecontactDALC, self).__init__()
        self.table = 'sitecontact'
        self.columns = (
            'siteID',
            'siteName',
            'contactId',
            'contact'
        )

class SiteinfoDALC(DALC):
    def __init__(self):
        super(SiteinfoDALC, self).__init__()
        self.table = 'siteinfo'
        self.columns = (
            'siteName',
            'siteID',
            'siteLevel'
        )

class StaffinfoDALC(DALC):
    def __init__(self):
        super(StaffinfoDALC, self).__init__()
        self.table = 'staffinfo'
        self.columns = (
            'staffID',
            'staffName',
            'contact'
        )

class TypeinfoDALC(DALC):
    def __init__(self):
        super(TypeinfoDALC, self).__init__()
        self.table = 'typeinfo'
        self.columns = (
            'name',
            'value'
        )

class UnitinfoDALC(DALC):
    def __init__(self):
        super(UnitinfoDALC, self).__init__()
        self.table = 'unitinfo'
        self.columns = (
            'unitModel',
            'unitName'
        )

