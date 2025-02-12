
'''
猜拳游戏：
    规则：对局10局，每胜一局得3分，平一局得1分，输一局不加分。

'''

import sys,time
from test3 import Ui_Dialog
from PyQt5.Qt import QApplication,QMainWindow,QTimer

#字典：根据双方各出现的结果来判断双方的得分情况
jieguo={
        "0 0":[1,1], "0 1":[3,0], "0 2":[0,3],
        "1 0":[0,3], "1 1":[1,1], "1 2":[3,0],
        "2 0":[3,0], "2 1":[0,3], "2 2":[1,1]

}

#玩家类：俩属性，一方法
class wanjia:
    def __init__(self):
        self.chuquan = 0
        self.fenzhi = 0
    def jiafen(self,value):
        self.fenzhi = self.fenzhi  + value

class mywin(QMainWindow, Ui_Dialog):

    #入口
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.n = 0  #机器人切换石头剪刀布定义的变量
        self.i = 10 #定义剩余的次数的变量

        # 清除输赢框
        self.jq_00.clear()
        self.me_00.clear()

        self.timer = QTimer()   # 创建一个QTimer实例，用于定时任务
        self.timer.timeout.connect(self.qiehuan)  # 将定时器的timeout信号连接到qiehuan槽函数，以便在定时器超时时执行
        self.timer.setInterval(50)  # 设置定时器的间隔时间为50毫秒
        self.timer.start()  # 启动定时器

        self.xz_1.clicked.connect(self.xuanze)
        self.xz_2.clicked.connect(self.xuanze)
        self.xz_3.clicked.connect(self.xuanze)
        self.clear2()
        self.me_1.show()
        self.xz_1.setChecked(True)
        self.pushButton.clicked.connect(self.pancai)

        self.jqr=wanjia()
        self.me=wanjia()

        self.sy.setText(str(self.i))


    def clear1(self):
        self.jq_1.hide()
        self.jq_2.hide()
        self.jq_3.hide()

    def clear2(self):
        self.me_1.hide()
        self.me_2.hide()
        self.me_3.hide()

    def qiehuan(self):
        self.clear1()
        sw = self.n % 3
        if sw == 0:
            self.jq_1.show()
            self.jqr.chuquan=0
        elif sw == 1:
            self.jq_2.show()
            self.jqr.chuquan=1
        elif sw == 2:
            self.jq_3.show()
            self.jqr.chuquan=2

        self.n+=1

    def xuanze(self):
        self.clear2()
        myclick = self.sender()
        if myclick == self.xz_1:
            self.me_1.show()    #点击“石头”，me对应的图片出现
            self.me.chuquan=0   #点击“石头”，将他
        elif myclick == self.xz_2:
            self.me_2.show()
            self.me.chuquan=1
        elif myclick == self.xz_3:
            self.me_3.show()
            self.me.chuquan=2

    def pancai(self):


        self.timer.stop()
        print(self.jqr.chuquan,self.me.chuquan)#机器人和me，出拳
        ls = str(self.jqr.chuquan)+' '+str(self.me.chuquan)#把“出拳”转成字符串
        jg=jieguo[ls]           #根据对局出拳，查出得分
        print(jg[0],jg[1])
        self.jqr.jiafen(jg[0])
        self.me.jiafen(jg[1])
        self.jq_df.setText(str(self.jqr.fenzhi))
        self.me_df.setText(str(self.me.fenzhi))

        if jg[0]>jg[1]:
            self.jq_00.setText("赢")
            self.me_00.setText("输")
        elif jg[0]<jg[1]:
            self.me_00.setText("赢")
            self.jq_00.setText("输")
        else:
            self.me_00.setText("平")
            self.jq_00.setText("平")
        QApplication.processEvents()    #刷新页面

        time.sleep(0.5)
        self.i -= 1
        self.sy.setText(str(self.i))
        self.timer.start()

if __name__ == '__main__':
    app = QApplication(sys.argv)#建立一个app对象
    my = mywin()            #建立一个my对象
    my.show()
    sys.exit(app.exec_())
