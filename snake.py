import time
from turtle import Turtle


class Snake:

    def __init__(self):

        self.segment = None
        self.x_cr = [0, -20*0.7, -40*0.7]
        self.all_segments = []
        self.head = None

    def create(self):

        for x in range(0, 3):
            self.segment = Turtle()
            self.segment.penup()
            self.segment.shape("square")
            self.segment.color('white')
            self.segment.shapesize(0.7, 0.7)
            self.segment.goto(x=self.x_cr[x], y=0)
            self.all_segments.append(self.segment)
        self.head = self.all_segments[0]

    def new_segment(self, position):

        self.segment = Turtle()
        self.segment.shapesize(0.7, 0.7)
        self.segment.penup()
        self.segment.shape("square")
        self.segment.color('white')
        self.segment.speed('fastest')
        self.segment.goto(position)
        self.all_segments.append(self.segment)

    def extend(self):
        self.new_segment(self.all_segments[-1].position())

    def link_segments(self):
        for _ in range(len(self.all_segments) - 1, 0, -1):
            x = self.all_segments[_ - 1].xcor()
            y = self.all_segments[_ - 1].ycor()
            self.all_segments[_].goto(x, y)
        self.head.forward(20*0.7)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)
        else:
            pass

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)
        else:
            pass

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)
        else:
            pass

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)
        else:
            pass

    def collision_with_wall(self):
        if self.head.xcor() > 288 or self.head.xcor() < -288 or self.head.ycor() < -288 or self.head.ycor() > 288:
            return False
        else:
            return True

    def game_over(self):
        for x in self.all_segments:
            x.hideturtle()
