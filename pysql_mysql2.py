#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author: tsunc & zadmine
@software: PyCharm Community Edition
@time: 2018/03/28 20:10

(E:\Users\lenovo\Anaconda2) C:\Users\lenovo>
#python e:\pymstaranchor\20180102\pysql_mysql.py
"""

from sqlalchemy import create_engine
import pymysql
import pandas as pd
import numpy as np

import matplotlib 
import matplotlib.pyplot as plt

import math


import sys
reload(sys)
sys.setdefaultencoding('utf-8')


pymysql.install_as_MySQLdb()
#engine = create_engine('mysql://root:ROOT@localhost:3306/iburks?charset=utf8')
engine = create_engine('mysql://root:ROOT@localhost:3306/iburks')

bankcards = pd.read_sql_query('select * from bankcards', engine)
#df = pd.DataFrame()

v_totalbhr = pd.read_sql_query('select * from v_totalbhr', engine)
#print v_totalbhr

v_licaitermed_mont = pd.read_sql_query('SELECT * FROM `v_licaitermed_mont` ORDER BY `TREALDATE` DESC', engine)
print v_licaitermed_mont.TREALDATE
print v_licaitermed_mont.T_stoHand
lc = v_licaitermed_mont.T_stoHand

v_banklicai_mont = pd.read_sql_query('SELECT * FROM `v_banklicai_mont`', engine)
print v_banklicai_mont.TREALDATE
print v_banklicai_mont.T_inHand
bk = v_banklicai_mont.T_inHand

#data1 = np.array(v_licaitermed_mont.TREALDATE)
lc_2 = np.array(lc[:24])
bk_2 = np.array(bk[:24])

print (lc_2)
print (bk_2)

##plt.plot(v_banklicai_mont.T_inHand)

#data = v_banklicai_mont.TREALDATE
suml = []
for i in range(len(lc_2)):
	s = 0
	lc = lc_2[i]
	bk = bk_2[i]
	s += lc
	s += bk
	suml.append(s/2)

print suml




index = np.arange(len(lc_2))

print (index)
##plt.plot( index, 'g-.', suml, 'b--' )
plt.plot( index, suml, 'r--' )

plt.bar(index, lc_2, color='w', label = 'lc', hatch = '****')
plt.bar(index, bk_2, color='w', label = 'bk', hatch = '----', bottom = lc_2)
#plt.barh(index, data3, color='w', label = 'c', hatch = '****', left=(data2))



plt.savefig('tmp.png')
plt.show()



'''
plt.plot(np.random.random(20))
data = np.arange(1, 5, 0.1)
print data


y1 = list(map(math.cos, math.pi * data))
y2 = list(map(math.cos, math.pi * data + math.pi / 2))
y3 = list(map(math.cos, math.pi * data - math.pi / 2))
#y1
plt.plot(data, y1, 'b--', data, y2, 'r-.', data, y3, 'gs')



#plt.figure(figsize=(500, 500)) 
plt.savefig('tmp.png')
plt.show()
'''
