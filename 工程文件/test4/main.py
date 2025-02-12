import requests,json
import sys
from test4 import Ui_Form
from PyQt5.Qt import  QApplication,QMainWindow,QTableView
from PyQt5 import QtCore,QtGui

class mywindows(QMainWindow,Ui_Form):
    def tianqi_cx(self):
        cityname=self.comboBox.currentText()    #城市名称选择
        #print(cityname)
        #print(self.city_no[cityname])
        url2 = 'http://t.weather.itboy.net/api/weather/city/%s'%(self.city_no[cityname])
        resp2 = requests.get(url2)
        resp2.encoding = 'utf-8'  # 汉字编码
        #print(resp2.text)
        res_json2 = resp2.json()
        print(res_json2['data']['forecast'])
        res_data2 =res_json2['data']['forecast']
        i=0
        for itme in res_data2:
            #print(itme)
            #print(itme['high'],itme['low'],itme['ymd'])

            #列表信息：
            self.qm.setItem(i, 0, QtGui.QStandardItem(itme['high']))
            self.qm.setItem(i, 1, QtGui.QStandardItem(itme['low']))
            self.qm.setItem(i, 2, QtGui.QStandardItem(itme['ymd']))
            self.qm.setItem(i, 3, QtGui.QStandardItem(itme['fx']))
            i+=1

    def city_code(self):
        url1 = 'http://img.weather.com.cn/newwebgis/fc/nation_fc24h_wea_2024092020.json'
        resp1 = requests.get(url1)
        resp1.encoding='utf-8'#汉字编码

        #print(resp1)
        #print(resp1.text)

        # 删除.json文件中开头的 webgisDot( 和结尾的 )
        res = resp1.text.replace('webgisDot(','').replace(')','')
        #print(res)
        res_json = json.loads(res)  #转成.json文件
        #print(res_json)
        res_data = res_json['data'] #保留data列表
        #print(res_data)

        # 字典：城市对应编码
        self.city_no={}
        for item in res_data:
            #print(item['namecn'],item['n'])    #提取城市名和编码
            self.comboBox.addItem(  item['namecn'])
            self.city_no[item['namecn']] = item['n']    #城市对应编码
        #print(self.city_no)


    def __init__(self):
        super().__init__()
        self.setupUi(self)

        #准备数据模型
        self.qm = QtGui.QStandardItemModel()

        #设置数据头栏名称
        self.qm.setHorizontalHeaderItem(0,QtGui.QStandardItem('日期'))
        self.qm.setHorizontalHeaderItem(1, QtGui.QStandardItem('高温'))
        self.qm.setHorizontalHeaderItem(2, QtGui.QStandardItem('低温'))
        self.qm.setHorizontalHeaderItem(3, QtGui.QStandardItem('天气情况'))

        #按照编号排序     #DescendingOrder(降序)    AscendingOrder(升序)
        self.qm.sort(0,QtCore.Qt.AscendingOrder)

        #将数据模型绑定到QTableView
        self.tableView.setModel(self.qm)

        self.city_code()
        self.pushButton.clicked.connect(self.tianqi_cx)

        self.tableView.setModel(self.qm)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    my = mywindows()
    my.show()
    sys.exit(app.exec_())
