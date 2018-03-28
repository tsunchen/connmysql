#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author: tsunc & zadmine
@software: PyCharm Community Edition
@time: 2018/03/28 20:10
"""

from sqlalchemy import create_engine
import pymysql
import pandas as pd
import numpy as np

import sys
reload(sys)
sys.setdefaultencoding('utf-8')


pymysql.install_as_MySQLdb()
#engine = create_engine('mysql://root:ROOT@localhost:3306/iburks?charset=utf8')
engine = create_engine('mysql://root:ROOT@localhost:3306/iburks')

s = pd.read_sql_query('select * from bankcards', engine)
#df = pd.DataFrame()
print s

t = pd.read_sql_query('select * from v_totalbhr', engine)
print t
