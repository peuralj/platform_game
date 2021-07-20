import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import QtWidgets, QtCore, QtGui

from game import *
from character_graphics import *
from leaderboard import *

class Graphics(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()
        

    def initUI(self):
        '''
        Open window. Add buttons. Add text. Place them.
        '''  
        #set text      
        self.qLabel = QLabel(self)
        self.qLabel.move(50, 100)
        self.qLabel.setText('Welcome to a platform game')
        self.qLabel.adjustSize()
        #set buttons
        self.start_button = QPushButton('Start Game', self)
        self.show_standings_button = QPushButton('Leaderboard', self)
        #set the places of buttons
        self.start_button.move(100, 150)
        self.show_standings_button.move(200, 150)
        #set the window
        self.setWindowTitle('Platform game') 
        self.resize(400,400)
        
        self.start_button.clicked.connect(self.give_name)
        self.show_standings_button.clicked.connect(self.show_standings)
           
        self.show()
        
    
    def show_standings(self):
        '''
        Open leaderboard
        '''
        self._new_window = NewWindow()
        self._new_window.show()
        
    def give_name(self):
        '''
        You can give your name and start playing.
        '''
        self.game = Game()
        
            
    def get_player(self):
        return player
            


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Graphics()
    #ex.activate_close()
    sys.exit(app.exec_())
    