# coding:utf-8


import mysql.connector
from Config import ReadConfig


rConfig = ReadConfig.ReadConfig()
mysql_info = rConfig.get_database()


class MysqlUtil():
    '''
    mysql数据库相关操作
    连接数据库信息：mysql_info
    创建表：mysql_execute
    插入一条记录：mysql_insert
    查询某个字段对应的字符串：mysql_getstring
    查询一组数据：mysql_getrows
    关闭mysql连接：mysql_close
    '''

    def __init__(self):
        self.db = mysql_info
        self.conn = MysqlUtil.__getConnector(self.db)

    @staticmethod
    def __getConnector(db):
        try:
            conn = mysql.connector.connect(host=db['host'],
                                           port=db['port'],
                                           user=db['username'],
                                           passwd=db['password'],
                                           database=db['database'],
                                           charset='utf8')
            return conn
        except Exception as a:
            print("数据库连接异常：%s" %a)

    def mysql_execute(self, sql):
        cur = self.conn.cursor()
        try:
            cur.execute(sql)
            cur.execute(sql)
        except Exception as a:
            print ("创建数据库失败:%s" %a)
        else:
            self.conn.close()

    def mysql_insert(self, sql):
        cur = self.conn.cursor()
        try:
            cur.execute(sql)
            self.conn.commit()
        except Exception as a:
            self.conn.rollback()
            print ("输出插入失败:%s" %a)
        else:
            self.conn.close()

    def mysql_getrows(self, sql):
        ''' 返回查询结果'''
        cur = self.conn.cursor()
        try:
            cur.execute(sql)
        except Exception as a:
            cur.rollback()
            print("执行SQL语句出现异常：%s"%a)
        else:
            rows = cur.fetchall()
            cur.close()
            return rows

    def mysql_getstring(self, sql):
        rows = self.mysql_getrows(sql)
        '''查询某个字段的对应值'''
        try:
            if rows != None:
                for row in rows:
                    for i in row:
                        return i
        except Exception as a:
            print ("查询失败：%s" %a)
        else:
            self.conn.close()




