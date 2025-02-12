#PyQt—restful API 获取云平台数据
#获取AccessToken
#使用AccessToken
#调用传感器数据API
#调用命令API

import sys
from untitled import Ui_MainWindow
from PyQt5.Qt import QApplication,QMainWindow,QTimer
import requests,json

class mywindow(QMainWindow,Ui_MainWindow):
    #读取传感器
    def read(self):
        url4 = 'http://api.nlecloud.com/Cmds?deviceId=1078584&apiTag=m_fan' #风扇api
        #温度模块
        url1 ='http://api.nlecloud.com/devices/1078584/sensors/z_temp'  #温度api网址
        resp1 = requests.get(url1,headers=self.header)
        #print(resp1.text)
        temp = resp1.json()['ResultObj']['Value']
        #print(temp)
        self.wendu.setText(str(temp))
        #控制特定温度打开/关闭电扇
        if temp>30:
            requests.post(url4, headers=self.header, json=1)
            self.on.show()
            self.off.hide()
        elif temp<30:
            requests.post(url4, headers=self.header, json=0)
            self.off.show()
            self.on.hide()
        #湿度模块
        url2 ='http://api.nlecloud.com/devices/1078584/sensors/z_humi'  #湿度api网址
        resp2 = requests.get(url2,headers=self.header)
        #print(resp2.text)
        humi = resp2.json()['ResultObj']['Value']
        #print(humi)
        self.shidu.setText(str(humi))

    #控制执行器
    def control(self):
        url3 ='http://api.nlecloud.com/Cmds?deviceId=1078584&apiTag=m_fan'
        key = self.sender()
        if key==self.kai:
            resp2 = requests.post(url3,headers=self.header,json=1)
            print(resp2.text)
            self.on.show()
            self.off.hide()
        elif key==self.guan:
            resp3 = requests.post(url3,headers=self.header,json=0)
            print(resp3.text)
            self.off.show()
            self.on.hide()

    def dingshi(self):
        self.read()
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.on.hide()      #默认显示亮的图片
        self.caiji.clicked.connect(self.read)
        self.kai.clicked.connect(self.control)
        self.guan.clicked.connect(self.control)

        #AccessToken
        url0 = 'http://api.nlecloud.com/Users/Login'
        data = {'Account':'账号','Password':'密码'}     #填写新大陆云平台的账号和密码
        resp0 = requests.post(url0,data=data)
        #print(resp0.text)
        token = resp0.json()['ResultObj']['AccessToken']
        #print(token)
        self.header = {'AccessToken':token}     #请求头

        #定时器
        self.time1 = QTimer()
        self.time1.timeout.connect(self.dingshi)
        self.time1.start(2000)  #1s

if __name__ == "__main__":
    app=QApplication(sys.argv)
    my=mywindow()
    my.show()
    sys.exit(app.exec_())



