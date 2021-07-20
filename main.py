import sys
from PyQt5.QtWidgets import QApplication

from graphics import *

def main():
    '''
    Creates the game and launches the Graphical User Interface.

    '''
    # Every Qt application must have one instance of QApplication.
    global app # Use global to prevent crashing on exit
    app = QApplication(sys.argv)
    graphics = Graphics()
    
    # Start the Qt event loop. (i.e. make it possible to interact with the graphics)
    sys.exit(app.exec_())

    # Any code below this point will only be executed after the graphics is closed.
    
    
if __name__ == '__main__':
    main()