import sys
import os
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import QtWidgets, QtCore, QtGui

from obstacle import *
from character_graphics import *
from graphics import *

class Game(QtWidgets.QMainWindow):
    
    def __init__(self):
        super().__init__()
        
        name, result = QInputDialog.getText(self, 'Name', 'Enter your name')
        if result == True:
            self.player = name
            self.curY = 0
            self.curX = 15
            self.speed = 8
            self.score = 0
            self.character = CharacterGraphics()
            self.obstacles = []
            self.create_game_window()
        
            self.timer = QTimer(self, interval=8)
            self.timer.timeout.connect(self.run)
            self.timer.start()
            
        
    def create_game_window(self):
        '''
        Sets up the game window.
        '''
        self.setWindowTitle('Game')
        self.show()

        # Add a scene for drawing 2d objects
        self.setGeometry(QtCore.QRect(0, 0, 900, 750))
        self.scene = QtWidgets.QGraphicsScene()
        self.scene.setSceneRect(0, 0, 800, 650)

        # Add a view for showing the scene
        self.view = QtWidgets.QGraphicsView(self.scene, self)
        self.view.setBackgroundBrush(QtGui.QColor("#99ccff"))
        self.view.adjustSize()
        self.view.show()
        self.horizontal = QtWidgets.QHBoxLayout()
        self.horizontal.addWidget(self.view)
        self.scene.addItem(self.character)
        self.character.setPos(self.curX,self.curY)
        
        
    def run(self):
        '''game loop'''
        self.drop_down()
        self.create_obstacles()
        self.move_obstacles()
        self.score += 1
    
    def mousePressEvent(self, event):
        self.scene.clear()
        self.view.viewport().update()
        i = 80
        j = 1
        help = 0
        new_file = 'new_leaderboard.txt'
        file_name = "leaderboard.txt"
        text = self.scene.addText('Your points:'+ str(self.score), QFont('Arial', 30))
        text.setPos(100, 0)
        text = self.scene.addText('Leaderboard:', QFont('Arial', 30))
        text.setPos(100, 50)
        with open(file_name, 'r') as read_obj, open(new_file, 'w') as write_obj:
            for line in read_obj:
                words = line.split()
                if help != 0:
                    line_print = (str(j)+". "+words[1]+ " "+ words[2]+ "\n")
                    write_obj.write(line_print)
                elif self.score >= int(float(words[2])):
                    line_print = (str(j)+ ". "+ self.player + " "+ str(self.score)+ "\n")
                    write_obj.write(line_print)
                    text = self.scene.addText(line_print, QFont('Arial', 30))
                    text.setPos(100, i)
                    help += 1
                    j+=1
                    i+=30
                    line_print = (str(j)+". "+words[1]+ " "+ words[2]+ "\n")
                    write_obj.write(line_print)
                else:
                    line_print = (str(j)+". "+words[1]+ " "+ words[2]+ "\n")
                    write_obj.write(line_print)
                text = self.scene.addText(line_print, QFont('Arial', 30))
                text.setPos(100, i)
                i+=30
                j+=1
                if j == 6:
                    break
        text = self.scene.addText('Close the window normally', QFont('Arial', 20))
        text.setPos(100, i+60)
        os.remove(file_name)
        os.rename(new_file, file_name)
        
    def drop_down(self):
        '''drops down the character'''
        if (self.speed == 8) or (self.speed == 0):
            on_obstacle = self.try_if_on_obstacle()
            if not on_obstacle:
                self.curY += self.speed
                self.character.setPos(self.curX, self.curY)
                self.update()
            
        elif self.speed == 15:
            self.jump += 1
            self.curY -= self.speed 
            self.character.setPos(self.curX, self.curY)
            self.update()
            if self.jump == 15:
                self.speed = 8
                self.jump = 0
            
    
    def keyPressEvent(self, space):
        '''character jumps'''
        if space.key() == Qt.Key_Space:
            self.speed = 15
            self.jump = 0
            
            
    def create_obstacles(self):
        "creeates obstacles every 80ms"
        if self.score%60 == 0:
            obstacle = Obstacle()
            self.scene.addItem(obstacle)
            self.obstacles.append(obstacle)
            obstacleX, obstacleY = obstacle.get_coodinates()
            obstacle.setPos(obstacleX, obstacleY)
            
        
    def move_obstacles(self):
        '''moves obstacles'''
        for obstacle in self.obstacles:
            obstacle.change_Xcoordinate()
            obstacleX, obstacleY = obstacle.get_coodinates()
            x2, y2 = self.get_pos(self.view, obstacle, (obstacle.boundingRect().bottomRight()))
            if x2 <= 0:
                self.obstacles.remove(obstacle)
            obstacle.setPos(obstacleX, obstacleY)
                
    def try_if_on_obstacle(self):
        '''checks if the character is on the obstacle'''
        if(len(self.obstacles) == 0):
            return False
        else:
            obstacle = self.obstacles[0]
            x, y = self.get_pos(self.view, obstacle, (obstacle.boundingRect().topLeft()))
            x2, y2 = self.get_pos(self.view, obstacle, (obstacle.boundingRect().bottomRight()))
        
            x_2, y_2 = self.get_pos(self.view, self.character, self.character.boundingRect().topLeft())
            x2_2, y2_2 = self.get_pos(self.view, self.character, self.character.boundingRect().bottomRight())
            lenght = x2_2 - x_2
    
            if(x <= x_2+lenght and x2 >= x2_2-lenght):
                if(y2_2+4 >= y and y2_2-4 <= y):
                    return True 
                elif y2_2+5 > y:
                    self.timer.stop()
                    gameover = self.scene.addText('Game Over', QFont('Arial', 100))
                    gameover.setPos(100, 150)
                    text_continue = self.scene.addText('Click anywhere to continue', QFont('Arial', 30)) 
                    text_continue.setPos(100, 250)
                    self.update()
                else:
                    return False

        
    def get_pos(game, view, item, point):
        '''
        Get the position in scene
        '''
        scenePos = item.mapToScene(point)
        viewportPos = view.mapFromScene(scenePos)
        viewPos = view.viewport().mapToParent(viewportPos)
        globalViewPos = view.mapToGlobal(QPoint(0, 0))
        return globalViewPos.x() + viewPos.x(), globalViewPos.y() + viewPos.y()
    
    