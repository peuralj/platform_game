from PyQt5 import QtWidgets, QtCore, QtGui
import random

class Obstacle(QtWidgets.QGraphicsPolygonItem):
    '''
    This creates the obstacles
    '''
    
    def __init__(self):
        super(Obstacle, self).__init__()
        
        black = QtGui.QColor(0, 0, 0)
        self.setBrush(black)
        
        self.posX = 750
        self.posY = random.randint(35, 100)
        self.random_lenght = random.randint(300, 400)
        
        self.create_obstacle()
        
    def create_obstacle(self):
        '''
        This creates the polygon aka obstacle in this case
        '''
        obstacle = QtGui.QPolygonF()
        
        obstacle.append(QtCore.QPointF(100, 400)) 
        obstacle.append(QtCore.QPointF(100, 500))
        obstacle.append(QtCore.QPointF(self.random_lenght, 500))
        obstacle.append(QtCore.QPointF(self.random_lenght, 400))

        self.setPolygon(obstacle)
        
    def change_Xcoordinate(self):
        self.posX -= 7
        
    def get_coodinates(self):
        return self.posX, self.posY

        