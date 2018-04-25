from tkinter import *
import random
from Sprite import Sprite
from Snake import Snake
from Collider import Collider
from Map import Map

# class application
# lay out our GUI
# parent is Frame

class Application(Frame):
    # class attributes
    matrix = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]


    WIDTH = 1000
    HEIGHT = 700
    IMAGE_SIZE = 60

    def __init__(self, window):
        super().__init__(window)
        self.grid() # display

        #build map
        map = Map(self.matrix, 50)
        self.WIDTH = map.getScreenWidth()
        self.HEIGHT = map.getScreenHeight()

        # Canvas - private instance variable
        self.__canvas = Canvas(self, width = self.WIDTH, height = self.HEIGHT, bg = "white")
        self.__canvas.grid()



        # Images - private instance variable
        self.snake = Snake(self.__canvas, 5, map.num2pixel(5), map.num2pixel(6))
        self.food = Sprite("goomba.gif", self.__canvas, 300, 300)

        # bind keyboard
        self.__canvas.bind("<Key>", self.key)
        # focus input on canvas
        self.__canvas.focus_set()
        self.start()

    def start(self):
        self.score = StringVar(self, 0)
        self.scoreVal = 0
        self.scoreText = self.__canvas.create_text(self.WIDTH - 120, self.HEIGHT/10, font = "Times 20 bold" ,text="score:")
        self.scoreText = self.__canvas.create_text(self.WIDTH - 50, self.HEIGHT/10, font = "Times 20 bold" ,text=self.score.get())
        self.update()

    def update(self):
        gameOver = False
        self.__canvas.itemconfig(self.scoreText, text = self.score.get())

        self.snake.snakeMove(self.snake.cur_dir)
        collider = Collider(self.__canvas)
        if collider.hasCollision(self.snake.spriteList[0].spriteEntity, self.food.spriteEntity):
            self.snake.eat()
            self.food.kill()
            self.randomFood()
            self.scoreVal += 1
            self.score.set(self.scoreVal)
        for i in range(1, len(self.snake.spriteList)):
            if collider.hasCollision(self.snake.spriteList[0].spriteEntity, self.snake.spriteList[i].spriteEntity):
                gameOver = True
        if not gameOver:
            self.snake.snakeOffScreen(self.WIDTH, self.HEIGHT, self.IMAGE_SIZE)
            self.after(150, self.update)
        else:
            text = self.__canvas.create_text(self.WIDTH/2, self.HEIGHT/2, font = "Times 30 bold" ,text="Game Over")

    def randomFood(self):
        row = int(self.HEIGHT/self.IMAGE_SIZE)
        col = int(self.WIDTH/self.IMAGE_SIZE)
        allPos = [i for i in range(row*col)]
        invalidPos = []
        for sprite in self.snake.spriteList:
            invalidPos.append(int(sprite.y/self.IMAGE_SIZE) * row + int(sprite.x/self.IMAGE_SIZE))
        valid = []
        for x in allPos:
            if x not in invalidPos:
                valid.append(x)
        x = int(valid[random.randint(0, len(valid)-1)]%col) * self.IMAGE_SIZE
        y = int(valid[random.randint(0, len(valid)-1)]/col) * self.IMAGE_SIZE
        self.food = Sprite("goomba.gif", self.__canvas, x,y)



    # # set up our key bindings
    def key(self, event):
        if event.keysym == "Up" or event.keysym == "w":
            self.snake.cur_dir = -1
        elif event.keysym == "Down" or event.keysym == "s":
            self.snake.cur_dir = 1
        elif event.keysym == "Left" or event.keysym == "a":
            self.snake.cur_dir = -2
        elif event.keysym == "Right" or event.keysym == "d":
            self.snake.cur_dir = 2

    #     # self.__canvas.update()
    #
    # def gameloop(self):
    #     self.after(200, self.gameloop)

def main():
    root = Tk()
    root.title("Mario game")
    root.geometry(str(Application.WIDTH)+"x"+str(Application.HEIGHT))
    app = Application(root)
    root.mainloop()


main()
