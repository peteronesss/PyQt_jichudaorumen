import sys

from untitled import Ui_Form

from PyQt5.QtWidgets import QApplication, QMainWindow


class mywindows(QMainWindow, Ui_Form):
    def jisuan(self):

        a = self.lineEdit.text()

        b = self.lineEdit_2.text()
        c = str(int(a) * int(b))

        self.lineEdit_3.setText(c)


    def __init__(self):
        super(mywindows, self).__init__()

        self.setupUi(self)

    # 连接信号与槽 connect代码

        self.pushButton.clicked.connect(self.jisuan)

if __name__ == '__main__':
    # 实例化，传参

    app = QApplication(sys.argv)

    # 创建对象

    mainWindow = mywindows()

    # 创建窗口

    mainWindow.show()

    # 进入程序的主循环，并通过exit函数确保主循环安全结束(该释放资源的一定要释放)

    sys.exit(app.exec_())