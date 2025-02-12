import sys
from test2 import Ui_Form

from PyQt5.Qt import QApplication, QMainWindow,QTimer
class mywindows(QMainWindow, Ui_Form):
    def clear(self):
        self.label.hide()
        self.label_2.hide()
        self.label_3.hide()
        self.label_4.hide()
        self.label_5.hide()
    def chuli(self):
        sw = self.n%5
        if sw == 0:
            self.clear()
            self.label.show()
        elif sw == 1:
            self.clear()
            self.label_2.show()
        elif sw == 2:
            self.clear()
            self.label_3.show()
        elif sw == 3:
            self.clear()
            self.label_4.show()
        elif sw == 4:
            self.clear()
            self.label_5.show()
        self.n += 1
    def __init__(self):
        super(mywindows, self).__init__()
        self.setupUi(self)
        self.n=0
        self.clear()
        self.time1 = QTimer()
        self.time1.timeout.connect(self.chuli)
        self.time1.start(200)
if __name__ == '__main__':
    # 实例化，传参
    app = QApplication(sys.argv)
    # 创建对象
    mainWindow = mywindows()
    # 创建窗口
    mainWindow.show()
    # 进入程序的主循环，并通过exit函数确保主循环安全结束(该释放资源的一定要释放)
    sys.exit(app.exec_())