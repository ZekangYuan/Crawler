#_*_codingcoding:utf-8_*_
'''
Created on 2016��8��6��

@author: sugo_yzk
����Pythonʹ��MySQL
'''
import MySQLdb
from sqlalchemy.sql import sqltypes

print MySQLdb

#1.�������Ӷ��󣬽���Python�ͻ��������������
conn = MySQLdb.connect(
                       host='127.0.0.1',
                       port=3306,
                       user='root',
                       passwd='123456',
                       db='imooc',
                       charset='utf8'
                       )

#2.��ȡ�α�
cursor = conn.cursor()

#3.ִ��sql���
print conn
print cursor

#ʹ��cursor.execute()ִ��select���
sql = "select * from user"
cursor.execute(sql)
print cursor.rowcount#��ȡ���������

rs = cursor.fetchone()#��ȡ��ǰ��һ������
print rs


rs = cursor.fetchmany(3)#��ȡ��������
print rs

rs = cursor.fetchall()#��ȡʣ�������
print rs

#ʹ��cursor.fetch*()��ȡ����������

#4.�ر���Դ
cursor.close()
conn.close()