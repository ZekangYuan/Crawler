#_*_codingcoding:utf-8_*_
'''
Created on 2016年8月6日

@author: sugo_yzk
测试Python使用MySQL
'''
import MySQLdb

print MySQLdb

#1.创建连接对象，建立Python客户端与网络的连接
conn = MySQLdb.connect(
                       host='127.0.0.1',
                       port=3306,
                       user='root',
                       passwd='123456',
                       db='imooc',
                       charset='utf8'
                       )

#2.获取游标
cursor = conn.cursor()

#3.执行sql语句
print conn
print cursor

#4.关闭资源
cursor.close()
conn.close()