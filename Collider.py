from tkinter import *

class Collider(object):

    def __init__(self, canvas):
        self.__canvas = canvas

    def hasCollision(self, entity1, entity2):
        coords = self.__canvas.bbox(entity1)
        collisions = self.__canvas.find_overlapping(coords[0], coords[1], coords[2], coords[3])
        if entity2 in collisions:
            return True
        return False

    def offScreen(self, width, height, image_size, entity):
        entityCoords = self.__canvas.bbox(entity)
        if entityCoords:
            if entityCoords[0] >= width:
                self.__canvas.move(entity, -width, 0)
            elif entityCoords[1] >= height:
                self.__canvas.move(entity, 0, -height)
            elif entityCoords[2] <= 0:
                self.__canvas.move(entity, width + image_size, 0)
            elif entityCoords[3] <= 0:
                self.__canvas.move(entity, 0, height)


