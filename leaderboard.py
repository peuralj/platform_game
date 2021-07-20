import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import QtWidgets, QtCore, QtGui


class NewWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(NewWindow, self).__init__()
        self._new_window = None
        file = open("leaderboard.txt", 'r')
        i = 50
        for line in file:
            self.qLabel = QLabel(self)
            self.qLabel.setText(line)
            self.qLabel.move(100, i)
            self.qLabel.setFont(QtGui.QFont("Times", 12, QtGui.QFont.Bold))
            self.qLabel.setAlignment(QtCore.Qt.AlignCenter)
            self.qLabel.adjustSize()
            i+=20
        self.setWindowTitle('Leaderboard')
        self.resize(400,400)
        file.close()


if __name__ == '__main__':
    app = QtGui.QApplication([])
    gui = NewWindow()
    gui.show()
    app.exec_()