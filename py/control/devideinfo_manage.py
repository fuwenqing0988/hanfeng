#!/usr/bin/python
# -*- coding: UTF-8 -*-
from manage import Manage
from py.dal.base_dal import DevideinfoDALC

class DevideinfoManager(Manage):
    def __init__(self):
        self.dal = DevideinfoDALC()

    def get_info_by_name(self,name):
        info = self.getInfo(key='devideName',value=name)
        return info


