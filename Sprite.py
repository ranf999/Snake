from tkinter import *

class Sprite(object):
    DIR_UP = -1
    DIR_DOWN = 1
    DIR_LEFT = -2
    DIR_RIGHT = 2
    def __init__(self, image_file_name, canvas, x, y):
        self.__canvas = canvas
        self.__image = PhotoImage(file = image_file_name)
        self.spriteEntity = canvas.create_image(x, y, image = self.__image)
        self.x = x
        self.y = y

    def move(self, dir, distance):
        if dir == self.DIR_UP:
            self.__canvas.move(self.spriteEntity, self.x, self.y - distance)
            self.setPosition(self.x, self.y - distance)
        if dir == self.DIR_DOWN:
            self.__canvas.move(self.spriteEntity, self.x, self.y + distance)
            self.setPosition(self.x, self.y + distance)
        if dir == self.DIR_LEFT:
            self.__canvas.move(self.spriteEntity, self.x - distance, self.y)
            self.setPosition(self.x - distance, self.y)
        if dir == self.DIR_RIGHT:
            self.__canvas.move(self.spriteEntity, self.x + distance, self.y)
            self.setPosition(self.x + distance, self.y)

    def setPosition(self, x, y):
        self.x = x
        self.y = y

    def getPosition(self):
        return self.x, self.y

    def kill(self):
        self.__canvas.delete(self.spriteEntity)

