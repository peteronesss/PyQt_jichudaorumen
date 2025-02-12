import re
from turtledemo.penrose import start
import requests,json,datetime
from PyQt5 import QtGui,QtCore

import sys
from urllib3.util.util import to_str
from test5 import Ui_MainWindow
from PyQt5.Qt import QApplication,QMainWindow,QTableView

class myWindows(QMainWindow,Ui_MainWindow):
    #第二步
    def chezhan_info(self):
        url1 = 'https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.9151'
        resp1 = requests.get(url1)
        resp1.encoding = 'utf8'
        #print(resp1.text)   #拼音缩写|站名称|站代码|全拼|站首写字母|站顺序号

        #检查请求状态
        if resp1.status_code == 200:

            #用正则表达式匹配数据（只要一部分）  \u表示以Unicode的编码格式    u4e00-u9fa5代表了符合汉字GB18030规范的字符集
            #正则提取字符串中的中文+‘|’+大写字母，+表示多个
            stations = re.findall('([\u4e00-\u9fa5]+)\|([A-Z]+)',resp1.text)
            #print(stations)
            #转成字典型
            self.stations_data = dict(stations)
            #print(self.stations_data)

            self.station_d = {}     #key与value进行互换
            for item in self.stations_data: #遍历每对键对应的键
                #print(item)
                self.station_d[self.stations_data[item]] = item   #根据键得到值，作为新字典的键；键为新字典的值
                self.comboBox1.addItem(item)    #车站信息存入下拉框
                self.comboBox2.addItem(item)
            print(self.stations_data)

        else:
            print('获取车站信息失败',resp1.status_code)
    #第三步车票查询
    def chepiao_cx(self):
        from_st = self.comboBox1.currentText()
        city_s = self.stations_data[from_st]        # 出发站
        to_st = self.comboBox2.currentText()
        city_e = self.stations_data[to_st]          # 到达站
        start_date = self.dateEdit.date().toString('yyyy-MM-dd')  # 时间   将/换成 -
        if self.radioButton1.isChecked():
            type = 'ADULT'
        elif self.radioButton2.isChecked():
            type = '0x00'
        #print(self.stations_data[from_st],self.stations_data[to_st],star_date,type)

        url2 = 'https://kyfw.12306.cn/otn/leftTicket/queryG?leftTicketDTO.train_date=%s&leftTicketDTO.from_station=%s&leftTicketDTO.to_station=%s&purpose_codes=%s'%(start_date,city_s,city_e,type)
        resp2 = requests.get(url2,headers=self.head)
        resp2.encoding = 'utf8'
        #print(resp2.text)


        data_json = resp2.json()#转换为json文件
        data_list = data_json['data']['result']
        #print(data_list)


        i=0
        for item in data_list:
            print(item)

            dt=item.split('|')

            #print(dt)
            print(dt[3],dt[6],dt[7],dt[30],dt[31],dt[32])
            self.qm.setItem(i,0,QtGui.QStandardItem(dt[3]))
            self.qm.setItem(i,1, QtGui.QStandardItem(dt[6]))
            self.qm.setItem(i,2, QtGui.QStandardItem(dt[7]))
            self.qm.setItem(i,3, QtGui.QStandardItem(dt[30]))
            self.qm.setItem(i,4, QtGui.QStandardItem(dt[31]))
            self.qm.setItem(i,5, QtGui.QStandardItem(dt[32]))
            i+=1

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        #第一步做表头
        self.qm = QtGui.QStandardItemModel()
        self.qm.setHorizontalHeaderItem(0,QtGui.QStandardItem('车次'))
        self.qm.setHorizontalHeaderItem(1, QtGui.QStandardItem('上车站'))
        self.qm.setHorizontalHeaderItem(2, QtGui.QStandardItem('下车站'))
        self.qm.setHorizontalHeaderItem(3, QtGui.QStandardItem('一等座'))
        self.qm.setHorizontalHeaderItem(4, QtGui.QStandardItem('二等座'))
        self.qm.setHorizontalHeaderItem(5, QtGui.QStandardItem('商务座'))
        self.tableView.setModel(self.qm)
        
        self.dateEdit.setDate(datetime.date.today())#取当前日期到出发日期
        self.radioButton1.setChecked(True)#默认的是普通票

        self.chezhan_info()
        self.pushButton.clicked.connect(self.chepiao_cx)
        
        #谷歌浏览器请求头
        self.head={   'Cookie':'JSESSIONID=9966BD9775C5622560DD11602BFF7DC0; guidesStatus=off; highContrastMode=defaltMode; cursorStatus=off; route=6f50b51faa11b987e576cdb301e545c4; BIGipServerotn=787481098.50210.0000; BIGipServerpool_passport=48497162.50215.0000',
                      'Host':'kyfw.12306.cn',
                      'Sec-Ch-Ua':'"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
                      'Sec-Ch-Ua-Mobile':'?0',
                      'Sec-Ch-Ua-Platform':'"Windows"',
                      'Sec-Fetch-Dest':'document',
                      'Sec-Fetch-Mode':'navigate',
                      'Sec-Fetch-Site':'none',
                      'Sec-Fetch-User': '?1',
                      'Upgrade-Insecure-Requests': '1',
                      'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'
                  }
        


if __name__ == "__main__":
    app = QApplication(sys.argv)
    my = myWindows()
    my.show()
    sys.exit(app.exec_())