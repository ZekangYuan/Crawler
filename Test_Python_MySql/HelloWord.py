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
conn.commit()
print cursor.rowcount#��ȡ���������

rs1 = cursor.fetchone()#��ȡ��ǰ��һ������
print rs1


rs2 = cursor.fetchmany(3)#��ȡ��������
print rs2

rs3 = cursor.fetchall()#��ȡʣ�������
print rs3


#ʹ��cursor.fetch*()��ȡ����������


#((5L, u'name5'), (6L, u'name6'), (7L, u'name7'), (8L, u'name8'), (9L, u'name9'))
#�Խ��ʹ�ö�ά����
#���ڽ����Ԫ�飬ʹ��Ԫ�����
rs4 = cursor.fetchall()
for row in rs4:
    print "userid=%s, username=%s" % row#ʹ��ģ���ַ������д�ӡ



#4.�ر���Դ  
cursor.close()
conn.close()