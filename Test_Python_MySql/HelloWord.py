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
conn.commit()
print cursor.rowcount#获取结果集个数

rs1 = cursor.fetchone()#获取当前第一条数据
print rs1


rs2 = cursor.fetchmany(3)#获取多条数据
print rs2

rs3 = cursor.fetchall()#获取剩余的数据
print rs3


#使用cursor.fetch*()获取并处理数据


#((5L, u'name5'), (6L, u'name6'), (7L, u'name7'), (8L, u'name8'), (9L, u'name9'))
#对结果使用二维遍历
#由于结果是元组，使用元组遍历
rs4 = cursor.fetchall()
for row in rs4:
    print "userid=%s, username=%s" % row#使用模板字符串进行打印



#4.关闭资源  
cursor.close()
conn.close()