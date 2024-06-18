from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.x = None
        self.y = None
        self.shape("circle")
        self.shapesize(0.5, 0.5)
        self.speed("fastest")
        self.color('blue')
        self.penup()
        self.x = random.randint(-280, 280)
        self.y = random.randint(-280, 280)
        self.coordinates = (self.x, self.y)
        self.goto(self.coordinates)

    def vanish(self):
        self.x = random.randint(-280, 280)
        self.y = random.randint(-280, 280)
        self.coordinates = (self.x, self.y)
        self.goto(self.coordinates)

    def game_over(self):
        self.hideturtle()

