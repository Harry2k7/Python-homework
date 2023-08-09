import sys
from PyQt5 import *
from PyQt5.QtWidgets import *

from call_standard import StandardPageWindow
from call_scientific import ScientificPageWindow



class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.resize(470,630)
        self.setFixedSize(470,630)
        self.layout = QGridLayout()
        self.setLayout(self.layout)

        self.layout.setContentsMargins(0,0,0,0)
        self.Stack = QStackedWidget()
        self.layout.addWidget(self.Stack)
        self.standardPageUi = StandardPageWindow()
        self.scientificPageUi = ScientificPageWindow()

        self.Stack.addWidget(self.standardPageUi)
        self.Stack.addWidget(self.scientificPageUi)

        self.scientificPageUi.chooseSignal.connect(self.showDialog)
        self.standardPageUi.chooseSignal.connect(self.showDialog)

    def showDialog(self,msg):
        if msg == 'standard':
            self.Stack.setCurrentIndex(0)
            self.standardPageUi.displayclear()
            self.standardPageUi.selectwindow.setCurrentIndex(0)
        elif msg == 'scientific':
            self.Stack.setCurrentIndex(1)
            self.scientificPageUi.selectwindow.setCurrentIndex(1)
            self.scientificPageUi.displayclear()
            self.scientificPageUi.selectwindow.setCurrentIndex(2)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())