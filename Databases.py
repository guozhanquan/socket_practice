import pymysql
import time
#接下来加入消息加解密功能和写入文件写入数据库功能就可以啦
def select_countfrom(table_name):
    db = pymysql.connect("localhost", "root", "root", "test", charset='utf8')
    cursor = db.cursor()
    cursor.execute("select count(*) from %s"%(table_name))
    return cursor.fetchone()[0]
count1=select_countfrom("dufa")+1
count2=select_countfrom("qunfa")+1
count3=select_countfrom("file")+1
count4=select_countfrom("log")+1
def getCurrentTime():
    return time.strftime("%Y-%m-%d-%H:%M:%S", time.localtime())
datee=getCurrentTime()
def insert_into_dufa(from_who,to_who,message1,datee):
    global count1
    db = pymysql.connect("localhost", "root", "root", "test", charset='utf8' )
    cursor = db.cursor()
    sql="insert into dufa values(%s,%s,%s,%s,%s)"
    cursor.execute(sql, (count1,from_who, to_who, datee, message1))
    # 提交到数据库执行
    db.commit()
    try:
        # 执行sql语句
        count1=count1+1
        print(count1)
        # 如果发生错误则回滚
    except:
        # 如果发生错误则回滚
        db.rollback()
        count1 = count1 - 1
    db.close()
# insert_into_dufa("王武","李四","hello",datee)
# 将从文件读出来的数据进行分割，然后写入到数据库中，
def insert_into_qunfa(from_who,datee,message1):
    global count2
    db = pymysql.connect("localhost", "root", "root", "test", charset='utf8' )
    cursor = db.cursor()
    sql = "insert into qunfa values(%s,%s, %s, %s)"
    try:
        # 执行sql语句
        count2=count2+1
        cursor.execute(sql, (count2, from_who, datee, message1))
        # 提交到数据库执行
        db.commit()
        # 如果发生错误则回滚
    except:
        # 如果发生错误则回滚
        db.rollback()
        count1 = count2 - 1
    db.close()
def insert_into_file(from_who,to_who,filename,datee):
    global count3
    db = pymysql.connect("localhost", "root", "root", "test", charset='utf8' )
    cursor = db.cursor()
    sql = "INSERT INTO file VALUES(%s,%s, %s, %s,%s)"
    # 提交到数据库执行
    db.commit()
    try:
        # 执行sql语句
        count3 = count3 + 1
        cursor.execute(sql, (count3, from_who, to_who, filename, datee))
        print(count3)
        # 提交到数据库执行
        db.commit()
        # 如果发生错误则回滚
    except:
        # 如果发生错误则回滚
        db.rollback()
        count3 = count3 - 1
    db.close()
#
# insert_into_file("张三","lisi","1111",datee)
def insert_into_log(datee,message):
    global count4
    db = pymysql.connect("localhost", "root", "root", "test", charset='utf8')
    cursor = db.cursor()
    sql = "INSERT INTO log VALUES(%s,%s, %s)"
    # 提交到数据库执行
    db.commit()
    try:
        # 执行sql语句
        count4 = count4 + 1
        cursor.execute(sql, (count4,datee,message))
        print(count4)
        # 提交到数据库执行
        db.commit()
        # 如果发生错误则回滚
    except:
        # 如果发生错误则回滚
        db.rollback()
        count4 = count4 - 1
    db.close()
