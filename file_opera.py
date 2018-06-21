import os
import time
from databases import *
def mkdir(path):
    folder = os.path.exists(path)

    if not folder:  # 判断是否存在文件夹如果不存在则创建为文件夹
        os.makedirs(path)  # makedirs 创建文件时如果路径不存在会创建这个路径
    else:
        pass
def init_file(filename):
    mkdir("D:/project_aa")
    file = open('D:/project_aa/' + filename + '.txt','a')
    file = open('D:/project_aa/' + filename + '.txt','a')
    file = open('D:/project_aa/' + filename + '.txt','a')
    file = open('D:/project_aa/' + filename + '.txt','a')
    file.close()
def getCurrentTime():
    return time.strftime("%Y-%m-%d-%H:%M:%S", time.localtime())
def write_into_file(filename,type,from_name,to_name,time_,send_file,message):
    with open("D:/project_aa/"+filename+".txt","a+") as f:
        content_file=type+" "+from_name+" "+to_name+" "+time_+" "+send_file+" "+message
        f.write(content_file+"\n")
def readFromFile(uni_name):
    file_name="D:/project_aa/"+uni_name+".txt"
    if os.path.exists(file_name):
        if os.path.getsize(file_name):
            print('文件存在且不为空')
            with open(file_name, "r+") as f:
                lines = f.readlines()  # 读取全部内容 ，并以列表方式返回
                for line in lines:
                    list_args = line.split()
                    if len(list_args) == 5:
                        if list_args[0] == "dufa":
                            # 执行写入独发的数据库
                            the_from = list_args[1]
                            the_to = list_args[2]
                            datee = list_args[3]
                            messg = list_args[4]
                            # 执行插入dufa数据库操作
                            insert_into_dufa(the_from, the_to, messg, datee)
                        elif list_args[0] == "file":
                            the_from = list_args[1]
                            the_to = list_args[2]
                            datee = list_args[3]
                            filename1 = list_args[4]
                            # 执行插入file数据库操作
                            insert_into_file(the_from, the_to, filename1, datee)
                        else:
                            print("正常情况下不会出现的情况")
                            pass
                    elif len(list_args) == 4:
                        # qunfa的情况
                        the_from = list_args[1]
                        datee = list_args[2]
                        messg = list_args[3]
                        # 执行插入qunfa表的情况
                        insert_into_qunfa(the_from, datee, messg)
                    elif len(list_args) == 3:
                        datee = list_args[1]
                        messg = list_args[2]
                        # 插入log数据库的情况
                        insert_into_log(datee, messg)
                    else:
                        print("应该不会出现的情况")
                        pass
                f.close()
                with open(file_name, "r+") as f:
                    f.truncate()
                    print("已经清空文件")

        else:
            print('文件存在且为空')
            pass

    else:
        print('文件不存在')
        init_file(uni_name)
        pass
