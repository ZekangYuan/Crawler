#coding:utf-8
import MySQLdb
import string

class kang:
    def __init__(self,filename):
        self.filename = filename
        self.num_list = []
        self.conn = MySQLdb.connect(
            host = '127.0.0.1',
            port = 3306,
            user = 'root',
            passwd = '123456',
            db = 'imooc',
            charset = 'utf8'
        )
        self.cursor = self.conn.cursor()
        # print self.conn
        # print self.cursor

    def read_file(self):
        for line in open(self.filename):
            if line != '' and line.find('@') != -1:
                print "取出的文本"
                print line
                self.process_raw_world(line)

    #获取了各字段的值
    def process_raw_world(self,line):
        # print type(line)
        self.num_list = []#此处要清空列表，否则会产生叠加
        tokens = line.split('@')
        for dev in tokens:
            if dev != '':
                # print dev.strip()
                ll = dev.strip().split()
                # print string.atof(ll[1])
                # print dev
                # print dev.find('\n')
                if dev.find('\n') != -1:
                    # print "找到了换行符"
                    # print type(dev)
                    # print dev
                    # print "去掉了换行符"
                    # print "________________________"
                    new_list =  list(dev)
                    changed =  "".join(new_list[0:15])
                    temp_list =  list(changed)
                    ss = changed.split(' ')
                    self.num_list.append(string.atof(ss[1]))
                    # print type(changed)
                    # print changed

                else:
                    # print type(string.atof(ll[1]))
                    self.num_list.append(string.atof(ll[1]))

        # print self.num_list.__len__()
        # print self.num_list[0]
        #如果这一纪录不在数据库才插入
        if self.isResist(self.num_list[0]) == 0:
            sql = "insert into phone_details values (%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f)"%tuple(self.num_list)
            #sql = "insert into phone_details values (2020064.0, 5.0, 0.0, 0.945, 3.0, 4.0, 0.026, 94.0, 0.029, 3.0, 142.0, 1220064.0, 38288.0, 2610.0, 4.0, 40898.0, 1160.0, 1160.0, 934.0, 43357.0, 5402.0, 1299.0, 0.0, 365.0);"
            print sql
            ret = self.cursor.execute(sql)
            self.conn.commit()
            # print '\n'
            print "成功插入================================="
            print("sql", sql)
            # print("insert ret ", ret)
            # print self.cursor.rowcount  # 获取结果集个数
            # print format

            # print "查询"
            # sql1 = "select * from phone_details;"
            # rs1 = self.cursor.execute(sql1)
            # self.conn.commit()
            # print rs1

    #负责关闭连接对象的游标
    def destr(self):
        
        self.cursor.close()
        self.conn.close()

    #判断该记录是否存在，存在返回1，不存在返回0
    def isResist(self,num):
        sql = "select * from phone_details where productId = %u"%int(num)
        re = self.cursor.execute(sql)
        print int(num)
        print "是否存在================================"
        print re
        if re == 0:
            return 0
        else:
            print int(num)
            print "已经存在"
            return  1




if __name__ == "__main__":
    too = kang("phoneonly_static.txt")
    too.read_file()
    too.destr()


