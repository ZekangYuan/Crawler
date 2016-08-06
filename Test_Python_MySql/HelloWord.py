#_*_codingcoding:utf-8_*_
'''
Created on 2016年8月6日

@author: sugo_yzk
测试Python使用MySQL
'''
import MySQLdb
from sqlalchemy.sql import sqltypes

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

#使用cursor.execute()执行select语句
sql = "select * from user"
cursor.execute(sql)
print cursor.rowcount#获取结果集个数

rs = cursor.fetchone()#获取当前第一条数据
print rs


rs = cursor.fetchmany(3)#获取多条数据
print rs

rs = cursor.fetchall()#获取剩余的数据
print rs

#使用cursor.fetch*()获取并处理数据

#4.关闭资源
cursor.close()
conn.close()