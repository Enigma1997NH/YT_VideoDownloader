#Gui for Downloading Video

# BY : Enigma1997NH

import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QWidget, QLabel, QLineEdit
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import QSize
from pytube import YouTube
import mainfile

class Main(QWidget):
    def __init__(self):
        #QMainWindow.__init__(self)
        super(Main,self).__init__()

        self.setMinimumSize(QSize(320,140))
        self.setWindowTitle("YT_Downloader")

        self.nameLabel = QLabel(self)
        self.nameLabel.setText('Link:')
        self.line = QLineEdit(self)

        self.line.move(80,20)
        self.line.resize(200,32)
        self.nameLabel.move(20,20)

        pybutton = QPushButton('DOWNLOAD',self)
        pybutton.clicked.connect(self.clickMethod)
        pybutton.resize(200,32)
        pybutton.move(80,60)

    def clickMethod(self):
        #print('Your Name: '+self.line.text())
        lin = self.line.text()
        mainfile.link(lin)


if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = Main()
    
    mainWin.show()
    sys.exit(app.exec_())
