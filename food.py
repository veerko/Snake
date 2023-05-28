import random
from turtle import Turtle


class Food(Turtle):
    def __init__(self):
        super().__init__()

        self.shape("circle")
        self.color("blue")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.refresh()

    def refresh(self):
        x_distance = random.randint(-280, 280)
        y_distance = random.randint(-280, 280)
        self.goto(x_distance, y_distance)
