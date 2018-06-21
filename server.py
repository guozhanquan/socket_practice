from PyQt4 import QtCore, QtGui
import sys
import socket
from threading import *
import time
import json

plainText=None
CipherText=None
DeCipherText=None

from databases import *
from file_opera import *

HOST = 'localhost'
PORT = 21565
BUFSIZE = 1024
ADDR = (HOST, PORT)
udpSerSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udpSerSock.bind(ADDR)
zidian = {}
msg_split = []
# 姓名列表
name_list = []
# (ip,port)列表
addr_list = []
key="qwwerrttooia"
from jiama import *
ipaddr = None
addr = None
msg_print = None
zidm = {}
readFromFile("log")
readFromFile("file")
readFromFile("dufa")
readFromFile("qunfa")
datee=getCurrentTime()


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

class Ui_Dialog(QtGui.QMainWindow):
    def __init__(self):
        super(Ui_Dialog, self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(685, 417)
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(60, 20, 211, 21))
        self.label.setObjectName(_fromUtf8("label"))
        self.pushButton = QtGui.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(410, 20, 75, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.textEdit = QtGui.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(10, 50, 661, 301))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.clickTestBtn)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.label.setText(_translate("Dialog", "服务器端", None))
        self.pushButton.setText(_translate("Dialog", "开启", None))
    def setTextEdit(self,message):
        self.textEdit.append(message)

    def clickTestBtn(self):
        ts = Thread(target=recv_fromCli)
        ts.setDaemon(True)
        ts.start()
        self.pushButton.setEnabled(False)
#按ESC关闭按钮
    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Escape:
            self.close()
    def logout(self):
        msg =  '服务器下线了'
        write_into_file("log", "log", " ", " ", datee, " ", msg)
        for i in zidm.values():
                msg = '服务器下线了'
                msg_print = msg
                ui_dialog.setTextEdit(msg_print)
                msg_encrypt = encrypt(json.dumps({'type': 'server_logout', 'msg': msg}), key)
                udpSerSock.sendto(msg_encrypt.encode('utf-8'), i)


    def closeEvent(self, event):
        reply = QtGui.QMessageBox.question(self, 'Message','Are you sure to quit?', QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
        if reply == QtGui.QMessageBox.Yes:
            time.sleep(1)
            self.logout()
            print("要关机了")
            event.accept()
        else:
            event.ignore()

class Dialog(QtGui.QDialog):
    def closeEvent(self, QCloseEvent):
        reply=QtGui.QMessageBox.question(self,'本程序',"是否要退出程序?",QtGui.QMessageBox.Yes|QtGui.QMessageBox.No,QtGui.QMessageBox.No)
        if reply == QtGui.QMessageBox.Yes:
            QCloseEvent.acccept()
        else:
            QCloseEvent.ignore()


app = QtGui.QApplication(sys.argv)
ui_dialog=Ui_Dialog()
ui_dialog.setFixedSize(700,453)


def recv_fromCli():
    global zidm
    global ipaddr
    global addr
    global name_list
    global datee
    msg_print = 'wait for the message...'
    ui_dialog.setTextEdit(msg_print)
    while True:
        try:
            data, addr = udpSerSock.recvfrom(1024)
        except:
            ui_dialog.setTextEdit("连接出现问题")
            write_into_file("log", "log", " ", " ", datee, " ", "服务器出错了")

        else:
            if addr not in addr_list:
                addr_list.append(addr)


            data = data.decode('utf-8')
            print('data=',type(data),data)
            json1 = decrypt(data,key)
            print('json1',json1)
            json1 = json.loads(json1)
            #解密
            print(json1)
            if json1['name'] != None:
                if json1['name'] not in name_list:
                    name_list.append(json1['name'])
            zidm = dict(zip(name_list, addr_list))  # ---------------------
            if json1['type'] == 'broadcast':
                for i in addr_list:
                    msg = json1['name'] + '对大家说' + json1['message']
                    ui_dialog.setTextEdit(msg)
                    msg_encrypt=encrypt(json.dumps({'type': 'broadcast', 'name':json1['name'],'msg': msg}),key)
                    udpSerSock.sendto(msg_encrypt.encode('utf-8'), i)
            elif json1['type'] == 'login':
                print(zidm)
                msg = json1['name'] + '成功上线了'

                write_into_file("log", "log", " ", " ", datee, " ",msg )
                msg_print = msg
                ui_dialog.setTextEdit(msg_print)
                for i in zidm.values():
                    msg_encrypt=encrypt(json.dumps({'type': 'login', 'msg': msg}),key)
                    udpSerSock.sendto(msg_encrypt.encode('utf-8'), i)
                    msg_encrypt=encrypt(json.dumps({'type':'update_userlist','msg':name_list}),key)
                    udpSerSock.sendto(msg_encrypt.encode('utf-8'),i)
            elif json1['type'] == 'logout':
                print(zidm)#---------------------
                name = json1['name']
                msg = json1['name'] + '下线了'
                write_into_file("log", "log", " ", " ", datee, " ", msg)

                port = int(json1['port'])
                addr_list.remove(addr_list[name_list.index(name)])
                name_list.remove(name)
                zidm.pop(name)#---------
                print(zidm)#------------
                #
                for i in zidm.values():
                    if i!=(json1['ip'], json1['port']):
                        msg = json1['name'] + '下线了'
                        msg_print = msg
                        ui_dialog.setTextEdit(msg_print)
                        msg_encrypt=encrypt(json.dumps({'type': 'logout', 'msg': msg}),key)
                        udpSerSock.sendto(msg_encrypt.encode('utf-8'), i)
                        msg_encrypt=encrypt(json.dumps({'type': 'update_userlist', 'msg': name_list}),key)
                        udpSerSock.sendto(msg_encrypt.encode('utf-8'), i)
            elif json1['type'] == 'filerequest':
                towhom = json1['towhom']
                from_who = json1['name']
                if towhom not in name_list:
                    msg_print = '用户列表中没有此人'
                    ui_dialog.setTextEdit(msg_print)
                    msg = None
                    msg_encrypt=encrypt(json.dumps({'type': 'fileresponse', 'msg': None}),key)
                    udpSerSock.sendto(msg_encrypt.encode('utf-8'), addr)
                else:
                    for i in name_list:
                        if towhom == i:
                            msg = addr_list[name_list.index(towhom)]
                            ipaddr = addr_list[name_list.index(from_who)]
                            msg_encrypt=encrypt(json.dumps({'type': 'fileresponse', 'msg': msg}),key)
                            udpSerSock.sendto(msg_encrypt.encode('utf-8'), ipaddr)
            elif json1['type'] == 'ppp_session_request':
                towhom = json1['from']
                from_who = json1['name']
                if towhom not in name_list:
                    msg_print = '用户列表中没有此人'
                    ui_dialog.setTextEdit(msg_print)
                    msg = None
                    msg_encrypt=encrypt(json.dumps({'type': 'ppp_session_response', 'msg': msg}),key)
                    udpSerSock.sendto(msg_encrypt.encode('utf-8'), addr)
                else:
                    msg = addr_list[name_list.index(towhom)]
                    msg_print = msg
                    ui_dialog.setTextEdit(str(msg_print))
                    msg_encrypt=encrypt(json.dumps({'type': 'ppp_session_response', 'msg': msg}),key)
                    udpSerSock.sendto(msg_encrypt.encode('utf-8'), addr)
            elif json1['type'] == 'show_all_users':
                msg_encrypt=encrypt(json.dumps({'type': 'show_response', 'info': name_list}),key)
                udpSerSock.sendto(msg_encrypt.encode('utf-8'), addr)

if __name__ == "__main__":
    icon = QtGui.QIcon()
    icon.addPixmap(QtGui.QPixmap("server.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    ui_dialog.setWindowIcon(icon)
    ui_dialog.show()
    ui_dialog.setWindowTitle("服务器端")
    sys.exit(app.exec_())
