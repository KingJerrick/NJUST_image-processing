import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import Qt
from slot.mainwindow import MainwindowAct





if __name__ == '__main__':
    # 界面的入口，在这里需要定义QApplication对象，之后界面跳转时不用重新定义，只需要调用show()函数jikt
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    app = QApplication(sys.argv)
    # 显示创建的界面
    MainWindow = MainwindowAct()  # 创建窗体对象
    MainWindow.setWindowIcon(QIcon("res/favicon.ico"))
    MainWindow.show()  # 显示窗体
    sys.exit(app.exec_())  # 程序关闭时退出进程


