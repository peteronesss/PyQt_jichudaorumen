import sys
from test2 import Ui_Form
from PyQt5.Qt import QApplication, QMainWindow,QTimer
class mywindows(QMainWindow, Ui_Form):
    #复位
    def clear(self):
        self.label.hide()
        self.label_2.hide()
    #开灯
    def kaiden(self):
        self.clear()
        self.label.show()
    #关灯
    def guanden(self):
        self.clear()
        self.label_2.show()
    #初始化：
    def __init__(self):
        super(mywindows, self).__init__()
        self.setupUi(self)
        self.n=0
        # 连接信号与槽 connect代码
        self.pushButton.clicked.connect(self.kaiden)
        self.pushButton_2.clicked.connect(self.guanden)
        self.clear()
if __name__ == '__main__':
    # 实例化，传参
    app = QApplication(sys.argv)
    # 创建对象
    mainWindow = mywindows()
    # 创建窗口
    mainWindow.show()
    # 进入程序的主循环，并通过exit函数确保主循环安全结束(该释放资源的一定要释放)
    sys.exit(app.exec_())
