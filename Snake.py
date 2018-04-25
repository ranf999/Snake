from Sprite import Sprite
from Collider import Collider

class Snake(object):
    DIR_UP = -1
    DIR_DOWN = 1
    DIR_LEFT = -2
    DIR_RIGHT = 2

    last_dir = DIR_UP
    cur_dir = DIR_UP

    foodList = []

    speed = 1


    def __init__(self, canvas, length, x, y):
        self.__canvas = canvas
        self.spriteList = []
        self.addOne = False
        for i in range(length):
            newSprite = Sprite("mario.gif", self.__canvas, x, y + i * 50)
            self.spriteList.append(newSprite)

    def snakeMove(self, dir):
        head_x, head_y = self.spriteList[0].getPosition()

        if self.addOne == True:
            self.add()
            self.addOne = False

        if dir == -self.last_dir:
            dir = self.last_dir
        if dir == self.DIR_UP:
            newSprite = Sprite("mario.gif", self.__canvas, head_x, head_y - 50)
            self.spriteList.insert(0, newSprite)
        elif dir == self.DIR_DOWN:
            newSprite = Sprite("mario.gif", self.__canvas, head_x, head_y + 50)
            self.spriteList.insert(0, newSprite)
        elif dir == self.DIR_LEFT:
            newSprite = Sprite("mario.gif", self.__canvas, head_x - 50, head_y)
            self.spriteList.insert(0, newSprite)
        elif dir == self.DIR_RIGHT:
            newSprite = Sprite("mario.gif", self.__canvas, head_x + 50, head_y)
            self.spriteList.insert(0, newSprite)
        self.spriteList.pop(-1)
        self.last_dir = dir

        if len(self.foodList) > 0:
            tail_x, tail_y = self.spriteList[-1].getPosition()
            if self.foodList[0][0] == tail_x and self.foodList[0][1] == tail_y:
                self.addOne = True
                self.foodList.pop(0)

    def eat(self):
        self.foodList.append([self.spriteList[0].x,self.spriteList[0].y])

    def add(self):
        tail_x, tail_y = self.spriteList[-1].getPosition()
        newSprite = Sprite("mario.gif", self.__canvas, tail_x, tail_y + 50)
        self.spriteList.append(newSprite)

    def gameOver(self):
        collider = Collider(self.__canvas)
        for i,sprite in enumerate(self.spriteList):
            if collider.hasCollision(self.spriteList[0].spriteEntity, sprite.spriteEntity):
                return True
        return False

    def snakeOffScreen(self, width, height, image_size):
        for i,sprite in enumerate(self.spriteList):
            entityCoords = self.__canvas.bbox(sprite.spriteEntity)
            if entityCoords:
                if entityCoords[0] >= width:
                    self.__canvas.move(sprite, -width, 0)
                    sprite.setPosition(sprite.x - width - image_size, sprite.y)
                elif entityCoords[1] >= height:
                    self.__canvas.move(sprite, sprite.x, sprite.y - height)
                    sprite.setPosition(sprite.x, sprite.y - height - image_size)
                elif entityCoords[2] <= 0:
                    self.__canvas.move(sprite, width + image_size, 0)
                    sprite.setPosition(sprite.x + width + image_size, sprite.y)
                elif entityCoords[3] <= 0:
                    self.__canvas.move(sprite, 0, height)
                    sprite.setPosition(sprite.x, sprite.y + height + image_size)


