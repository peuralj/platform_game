from PyQt5 import QtWidgets, QtCore, QtGui

class CharacterGraphics(QtWidgets.QGraphicsPolygonItem):
    '''
    This class creates the character.
    '''
    
    def __init__(self):
        super(CharacterGraphics, self).__init__()
        
        blue = QtGui.QColor(0, 0, 200)
        self.setBrush(blue)
        
        self.square_size = 50
        
        self.create_polygon()
        
    def create_polygon(self):
        '''
        This creates the polygon aka character in this case
        '''
        polygon = QtGui.QPolygonF()
        
        polygon.append(QtCore.QPointF(100, 100)) # Top-left
        polygon.append(QtCore.QPointF(100, 100+self.square_size)) # Bottom-left
        polygon.append(QtCore.QPointF(100+self.square_size, 100+self.square_size)) # Bottom-right
        polygon.append(QtCore.QPointF(100+self.square_size, 100)) # Top-right

        self.setPolygon(polygon)

