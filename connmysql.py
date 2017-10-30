#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author: tsunc & zadmine
@software: PyCharm Community Edition
@time: 2017/10/30 10:10

"""


import pymysql.cursors

#50.62.209.86>>>


def connmysql(host, user, passwd, db, sentence):
	conn = pymysql.connect(host,user,passwd,db)
	cur = conn.cursor()
	reCount = cur.execute(sentence)
	print reCount
	conn.close()


def connmysql_fetchall(host, user, passwd, db,sentence):
	conn = pymysql.connect(host,user,passwd,db)
	cur = conn.cursor()
	reCount = cur.execute(sentence)
	data = cur.fetchall()
	for d in data:
		print d
	cur.close()
	conn.close()


def connmysql_fetchallDictCursor(host, user, passwd, db,sentence):
	conn = pymysql.connect(host,user,passwd,db,cursorclass=pymysql.cursors.DictCursor)
	cur = conn.cursor()
	reCount = cur.execute(sentence)
	data = cur.fetchall()
	for d in data:
		print d
	cur.close()
	conn.close()



if __name__=='__main__':
    #test_webpage('https://www.juaicai.cn')
    print ("+--line of split--+")
    connmysql('50.62.209.86','adminidc','idc_21viacloud','tsun_chen_idc','select * from idc_09_k01')
    print ("+--line of split--+")
    connmysql_fetchall('50.62.209.86','adminidc','idc_21viacloud','tsun_chen_idc','select * from idc_09_k01')
    print ("+--line of split--+")
    connmysql_fetchallDictCursor('50.62.209.86','adminidc','idc_21viacloud','tsun_chen_idc','select * from idc_09_k01')
    
