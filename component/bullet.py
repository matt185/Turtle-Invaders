from turtle import Turtle
import math

BULLET_SPEED = 30


class Bullet(Turtle):
    def __init__(self):
        super().__init__()
        self.bullet_state = "ready"
        self.color("yellow")
        self.shape("arrow")
        self.penup()
        self.speed(0)
        self.setheading(90)
        self.shapesize(0.5, 0.5)
        self.hideturtle()
        self.x = 0
        self.y = 0

    def fire_bullet(self):
        if self.bullet_state == "ready":
            self.bullet_state = "fire"
            self.setposition(self.x, self.y)
            self.showturtle()

    def move_bullet(self):
        # Move the bullet
        if self.bullet_state == "fire":
            y = self.ycor()
            y += BULLET_SPEED
            self.sety(y)
        # Check to see if the bullet has gone to the top
        if self.ycor() > 275:
            self.hideturtle()
            self.bullet_state = "ready"
