from turtle import Screen, Turtle
import time

# Setup the field
from component.bullet import Bullet
from component.monster import Monster
from component.player import Player
from component.score import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Turtle Invaders")
screen.tracer(0)

# Create the player
player = Player()

# Create the monsters
monster = Monster()

# Create the bullet
bullet = Bullet()

# Create the score board
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.right, "Right")
screen.onkey(player.left, "Left")
screen.onkey(bullet.fire_bullet, "space")

game_over = False

while not game_over:
    screen.update()
    time.sleep(0.01)
    
    if bullet.bullet_state == "ready":
        bullet.x = player.xcor()
        bullet.y = player.ycor() + 10
        
    monster.move_monsters()
    bullet.move_bullet()
    
    monster.check_collision(bullet, player, scoreboard)
    if monster.collision:
        game_over = True

screen.exitonclick()
