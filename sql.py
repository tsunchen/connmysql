# -*- coding:utf-8 -*-

"""
@author: tsunc & zadmine
@software: PyCharm Community Edition
@time: 2017/11/3 10:10

#update 2017/11/15

#update 2017/11/18
 fetchone by port, scabip
 return unique

"""


import pymysql.cursors

#50.62.209.86>>>


def connmysql_fetchoneDictCursor(host, user, passwd, db, parameters):
        conn = pymysql.connect(host,user,passwd,db,cursorclass=pymysql.cursors.DictCursor)
        cur = conn.cursor()

        sql = "select description, emailhead, port, line, speed, scabip from idc_09_sharecab where port=%s and scabip=%s"
        #parameters = ('B-NX', 'Fa0/XX', 'Desc', 'Speed 10')

        reCount = cur.execute(sql, parameters)
        #print "reCount: %s" % reCount
        '''
        data = cur.fetchall()
        for d in data:
                print d
        '''
        data = cur.fetchone()
        cur.close()
        conn.close()
        return data


if __name__=='__main__':
    print ("+--line of split--+")
    parameters_fone = ('FastEthernet0_21'.replace("_","/"),'211.152.53.190')
    connmysql_fetchoneDictCursor('50.62.209.86','adminidc','idc_21viacloud','tsun_chen_idc', parameters_fone)
