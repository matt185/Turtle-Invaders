from turtle import Turtle

STARTING_POSITION = (0, -250)
PLAYER_SPEED = 15


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.color("yellow")
        self.shape("triangle")
        self.penup()
        self.speed(0)
        self.setposition(STARTING_POSITION)
        self.setheading(90)

    def left(self):
        x = self.xcor()
        x -= PLAYER_SPEED
        if x < -280:
            x = -280
        self.setx(x)

    def right(self):
        x = self.xcor()
        x += PLAYER_SPEED
        if x > 280:
            x = 280
        self.setx(x)
