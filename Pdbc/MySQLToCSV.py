#-*- coding:utf-8 -*-
import MySQLdb
import os
#防止读取MySQL中文端时出现问题
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import csv

class MySQLToCSV:
    def __init_db(self):
        self._mysql_db = MySQLdb.connect(host="188.188.20.191",user="boch",passwd="123456",port=3306,db="qlytest",charset="utf8")
        self.mysql_cur = self._mysql_db.cursor()
        self.seq = 0

    def __init__(self):
        self.__init_db()

    def _release_db(self):
        self.mysql_cur.close()
        self._mysql_db.close()

    def _do(self):
        self.mysql_cur.arraysize = 50
        select_sql = "select name,nickname from b_account"
        print select_sql
        self.mysql_cur.execute(select_sql)
        count=0
        csvfile = file('MySQLToCSV.csv','wb')
        print dir(csv)
        writers = csv.writer(csvfile)
        writers.writerow(['name','nickname'])
        while 1:
            lines = self.mysql_cur.fetchmany(50)
            if len(lines)==0:
                break
            for i in lines:
                print i
                writers.writerows([i])
        csvfile.close()


if __name__=="__main__":
    p = MySQLToCSV()
    p._do()
    p._release_db()
