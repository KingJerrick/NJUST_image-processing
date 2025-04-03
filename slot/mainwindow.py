import ui.ui_mainwindow
from PyQt5.QtWidgets import QMainWindow, QStackedLayout
from slot.equhist import equhistAct
from slot.DCT import DCTAct
from slot.DFT import DFTAct

class MainwindowAct(QMainWindow,ui.ui_mainwindow.Ui_MainWindow):
    def __init__(self):
        super(MainwindowAct, self).__init__()
        self.setupUi(self)

        self.stackedLayout = QStackedLayout(self.frame)
        self.DCTPage = DCTAct()
        self.stackedLayout.addWidget(self.DCTPage)
        self.DFTPage = DFTAct()
        self.stackedLayout.addWidget(self.DFTPage)
        self.equhistPage = equhistAct()
        self.stackedLayout.addWidget(self.equhistPage)

        self.pushButton.clicked.connect(self.Show)
        self.pushButton_2.clicked.connect(self.Show)
        self.pushButton_3.clicked.connect(self.Show)

    def Show(self):
        sender = self.sender().objectName()
        index = {
            "pushButton": 0,
            "pushButton_2": 1,
            "pushButton_3": 2,
        }
        self.stackedLayout.setCurrentIndex(index[sender])