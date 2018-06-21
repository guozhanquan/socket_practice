from PyQt4 import QtCore, QtGui
import sys
from socket import *
from threading import *
import socket
import random
import json
import  os

kilobytes = 1024
import time
import os
ipAddr = None
ipAddr_to = None
ipAddr_to_file = None
flag_send = None
file_addr = None
HOST = 'localhost'
# 发送人的名字
name = None
flag = False
duixiang="ALL"
file_name=None
key="qwwerrttooia"
plainText=None
CipherText=None
DeCipherText=None
from  file_opera import *
from databases import *
from jiama import *
import threading

def getCurrentTime():
    return time.strftime("%Y-%m-%d-%H:%M:%S", time.localtime())

#一开始执行文件写入数据库功能，然后把文件删除
readFromFile("log")
readFromFile("file")
readFromFile("dufa")
readFromFile("qunfa")
datee=getCurrentTime()
def IsOpen(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect(('127.0.0.1', int(port)))
        s.shutdown(2)
        return True
    except:
        return False


def ProduceAndCheckPort():
    while True:
        port = random.randint(1025, 65536)
        if IsOpen(port):
            pass
        else:
            break
    return port


port = ProduceAndCheckPort()
udpCliSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udpCliSock.bind(('127.0.0.1', port))
benji_ipaddr = ('127.0.0.1', port)

def isDecode(recvInfos):
    global flag
    try:
        recvInfo = recvInfos.decode('utf-8')
        recvInfo1=decrypt(recvInfo,key)
        data = json.loads(recvInfo1)
    except:
        flag = False
    else:
        flag = True

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)


def sendfile(file_path):
    file = open(file_path, 'rb')
    while True:
        chunk = file.read(1024)
        if not chunk:
            break
        udpCliSock.sendto(chunk, ipAddr_to_file)
        time.sleep(0.3)
class Ui_Dialog(QtGui.QMainWindow):
    global port
    global ipAddr
    global ipAddr_to
    global ipAddr_to_file
    global benji_ipaddr
    global duixiang
    global file_name
    global datee
    def __init__(self):
        super(Ui_Dialog, self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(808, 544)
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(140, 10, 91, 31))
        self.label.setObjectName(_fromUtf8("label"))
        self.lineEdit = QtGui.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(240, 20, 151, 20))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.pushButton = QtGui.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(400, 20, 75, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.textEdit = QtGui.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(240, 70, 551, 381))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(660, 10, 141, 20))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.toolButton = QtGui.QToolButton(Dialog)
        self.toolButton.setGeometry(QtCore.QRect(670, 40, 111, 20))
        self.toolButton.setObjectName(_fromUtf8("toolButton"))
        self.pushButton_2 = QtGui.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(650, 460, 141, 41))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.lineEdit_2 = QtGui.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(10, 460, 631, 41))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(60, 40, 121, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_4 = QtGui.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(510, 10, 131, 20))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.lineEdit_3 = QtGui.QLineEdit(Dialog)
        self.lineEdit_3.setGeometry(QtCore.QRect(510, 40, 131, 20))
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.listWidget = QtGui.QListWidget(Dialog)
        self.listWidget.setGeometry(QtCore.QRect(0, 71, 231, 381))
        self.listWidget.setObjectName(_fromUtf8("listWidget"))

        self.retranslateUi(Dialog)
        self.pushButton.clicked.connect(self.login_func)
        self.toolButton.clicked.connect(self.file_send)
        self.pushButton_2.clicked.connect(self.send_message)
        # self.listWidget.selectionChanged.connect(self.listwidge11)
        # self.listWidget.itemChanged.connect(self.listwidge11)
        self.listWidget.itemDoubleClicked.connect(self.doubleclick)
        self.listWidget.itemClicked.connect(self.clickevent)

        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def setTextEdit(self,message):
        self.textEdit.append(message)

    def setButtonFalse(self,flag):
        if flag ==True:
            self.pushButton.setEnabled(False)
        else:
            pass
    def send_message(self):
        global duixiang
        global name
        global towhom
        global key
        global datee
        time.sleep(0.5)
        #对象不为空
        message=self.lineEdit_2.text()
        if duixiang == "ALL":
            #群发
            time1=str(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
            messg=time1+"\n"+"群发"
            self.textEdit.append(messg)
            #验证消息非空
            if not message:
                self.textEdit.append('no message')
            else:
                              msg_encrypt=encrypt(json.dumps({'type': 'broadcast', 'name': name, 'ip': '127.0.0.1', 'port': port,'message': message}),key)
                udpCliSock.sendto(msg_encrypt.encode("utf-8"),(HOST, 21565))
        else:
            #独发
            time1 = "["+str(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))+"]"
            messg = time1 + "\n" + "独发"
            self.textEdit.append(messg)
            towhom = duixiang
            x=encrypt(json.dumps({'type': 'ppp_session_request', 'from': towhom, 'name': name}),key)
            udpCliSock.sendto(x.encode('utf-8'),(HOST, 21565))
            time.sleep(0.5)
            #从服务器端获取要发送人的地址ipAddr_to
            if ipAddr_to != None:
                message = self.lineEdit_2.text()
                if  message:
                    self.textEdit.append(message)
                    msg_encrypt=encrypt(json.dumps({'type': 'ppp_session_send', 'msg': message, 'from': towhom, 'name': name}),key)
                    udpCliSock.sendto(msg_encrypt.encode('utf-8'),ipAddr_to)
                else:
                    self.textEdit.append("消息不能为空")
    def doubleclick(self):
        print("您双击了按钮")
    def clickevent(self):
        global duixiang
        # print("选中了",self.listWidget.currentItem().text())
        self.textEdit.append(self.listWidget.currentItem().text())
        duixiang=self.listWidget.currentItem().text()
#推出线程
    def logout(self):
        self.textEdit.append(name+'下线了')
        msg_encrypt=encrypt(json.dumps({'type': 'logout', 'name': name, 'ip': '127.0.0.1', 'port': port}),key)
        udpCliSock.sendto(msg_encrypt.encode('utf-8'),(HOST, 21565))
        self.listWidget.clear()
    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Escape:
            self.logout()
            print("要关机了")
            udpCliSock.close()
            self.close()
    def login_func(self):
        # 开启接受线程
        ts = Thread(target=recvData)
        ts.setDaemon(True)
        ts.start()
        global name
        if name == None:
            self.textEdit.append('输入你的用户名')
            name = self.lineEdit.text().strip()
            while True:
                if not name:
                    pass
                else:
                    msg_encrypt=encrypt(json.dumps({'type': 'login', 'name': name, 'ip': '127.0.0.1', 'port': port}),key)
                    print(msg_encrypt.encode('utf-8'))
                    udpCliSock.sendto(msg_encrypt.encode('utf-8'),(HOST, 21565))
                break
        else:
            messg=time1=str(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))+"\n"+name + '欢迎回来'
            self.textEdit.setText(messg)
    def update_Items(self,list):
        #更新用户列表
        self.listWidget.clear()
        self.listWidget.insertItem(-1,"ALL")
        #除掉自己的名字
        list.remove(name)
        self.listWidget.addItems(list)
        self.listWidget.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.listWidget.setCurrentRow(-1)
    def file_send(self):
        global  ipAddr_to_file
        duixiang = self.lineEdit_3.text().strip()
        msg_encrypt=encrypt(json.dumps({'type': 'filerequest', 'towhom': duixiang, 'name': name}),key)
        udpCliSock.sendto(msg_encrypt.encode('utf-8'),(HOST, 21565))
        time.sleep(1)
        # 后续验证代码待续
        if ipAddr_to_file != None:
            file_name = QtGui.QFileDialog.getOpenFileName(self, 'Open file', './')
            # 先把一些基本信息发过去
            print(file_name)
            msg_encrypt=encrypt(json.dumps({'type': 'ppp_file_send_ok', 'name': name,'from1':duixiang,'file_name': file_name,
                            'ipaddr': ipAddr_to_file}),key)
            udpCliSock.sendto(msg_encrypt.encode('utf-8'), ipAddr_to_file)
write_into_file("file","file",name,duixiang,datee,file_name," ")
            self.textEdit.append("您已经向"+duixiang+"发送了一个文件"+file_name)

            file_thread=threading.Thread(target=sendfile,args=(file_name,))
            file_thread.setDaemon(True)
            file_thread.start()
        else:
            self.textEdit.append('没有此人')

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.label.setText(_translate("Dialog", "请输入你的名字", None))
        self.pushButton.setText(_translate("Dialog", "确定", None))
        self.label_3.setText(_translate("Dialog", "请选择要发送的文件", None))
        self.toolButton.setText(_translate("Dialog", "...", None))
        self.pushButton_2.setText(_translate("Dialog", "发送", None))
        self.label_2.setText(_translate("Dialog", "用户列表", None))
        self.label_4.setText(_translate("Dialog", "请输入文件发送的对象", None))
    def closeEvent(self, event):
        reply = QtGui.QMessageBox.question(self, 'Message','Are you sure to quit?', QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
        if reply == QtGui.QMessageBox.Yes:
            time.sleep(1)
            self.logout()
            print("要关机了")
            event.accept()
        else:
            event.ignore()

app = QtGui.QApplication(sys.argv)
ui_dialog = Ui_Dialog()
ui_dialog.setFixedSize(820,570)

#创建文件夹函数
def mkdir(path):
    folder = os.path.exists(path)

    if not folder:  # 判断是否存在文件夹如果不存在则创建为文件夹
        os.makedirs(path)  # makedirs 创建文件时如果路径不存在会创建这个路径
    else:
        pass
    # 接受线程
def recvData():
    global ipAddr_to
    global ipAddr_to_file
    global benji_ipaddr
    global flag
    global file_addr
    global name
    global datee

    while True:
        try:
            recvInfos, addr = udpCliSock.recvfrom(1024)
        except:
            ui_dialog.setTextEdit("服务器可能没有打开")
            #写入日志记录文件
            name=None
        else:
            isDecode(recvInfos)
            if flag == True:
                #先解密
                recvInfo = recvInfos.decode('utf-8')
                recvInfos=decrypt(recvInfo,key)
                data = json.loads(recvInfos)
                print(data)
                if data['type'] == 'broadcast':
                    name=data['name']
                    time1=getCurrentTime()
                    ui_dialog.setTextEdit(time1+"\n")
                    ui_dialog.setTextEdit(data['msg'])
                    write_into_file("qunfa","qunfa",name," ",datee," ",data['msg'])
                elif data['type'] == 'login':
                    # 服务器返回来的通知登录消息
                    ui_dialog.setTextEdit('下面是登录消息'+data['msg'])
                elif data['type'] == 'logout':
                    time1 = "["+str(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))+"]"
                    messg=time1+'下面是注销消息'+data['msg']
                    ui_dialog.setTextEdit(messg)
                elif data['type'] == 'server_logout':
                    ui_dialog.setTextEdit("服务器已关闭，所有用户被强制下线")
                    udpCliSock.close()
                #     显示注销信息
                elif data['type'] == 'fileresponse':
                    # 服务器返回来的请求发送人的ipAddr
                    if data['msg'] != None:
                        ipAddr_to_file = tuple(data['msg'])
                    else:
                        ui_dialog.setTextEdit('用户列表中没有此人')
                elif data['type'] == 'ppp_session_response':
                    ipAddr_to = tuple(data['msg'])
                elif data['type'] == 'ppp_session_send':
                    from_who = data['from']
                    name = data['name']
                    msg = data['msg']
                    message=name+ '对'+ from_who+ '说'+ msg
                    time1 = "[" + str(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))) + "]"
                    ui_dialog.setTextEdit(time1+"\n")
                    ui_dialog.setTextEdit(message)
                    write_into_file("dufa","dufa",name,from_who,datee," ",msg)

                elif data['type'] == 'ppp_file_send_ok':
                    name = data['name']
                    from_who=data['from1']#文件要发给谁
                    file_name = data['file_name']
                    print(file_name)
                    file_name = file_name.split("/")
                    print(file_name)
                    #判断该路径下有无该文件，如果没有就创建
                    mkdir('D:/savefile_worksapce')
                    file_addr = 'D:/savefile_worksapce/' + file_name[-1]
                    ipAddr_to_file = data['ipaddr']
                    write_into_file("file","file",name,from_who,datee,file_name[-1], " ")
                    ui_dialog.setTextEdit(name+"向"+from_who+"发送了一个文件"+file_name[-1])

                elif data['type'] == 'show_response':
                    # 返回所有用户名
                    info = data['info']
                elif data['type'] == "update_userlist":
                    # 更新列表信息
                    user_list = data['msg']
                    #传入的是一个列表
                    ui_dialog.update_Items(user_list)
            else:
                with open(file_addr, 'ab') as fp:
                    fp.write(recvInfos)
                print('执行完了写文件')
#                 在这里添加一个收文件的记录
if __name__ == "__main__":
    icon = QtGui.QIcon()
    icon.addPixmap(QtGui.QPixmap("client.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    ui_dialog.setWindowIcon(icon)
    ui_dialog.show()
    ui_dialog.setWindowTitle("客户端")
    sys.exit(app.exec_())
