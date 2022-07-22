from turtle import Turtle
import random
import math

num_monster = 5


def is_collision(ele, monster):
    distance = math.sqrt(math.pow(ele.xcor() - monster.xcor(), 2) + math.pow(ele.ycor() - monster.ycor(), 2))
    if distance < 15:
        return True
    else:
        return False


class Monster:
    def __init__(self):
        self.colors = ["red", "green", "blue", "yellow", "purple"]
        self.monsters = []
        self.create_monsters()
        self.monster_speed = 2
        self.collision = False

    def create_monsters(self):
        for _ in range(num_monster + 1):
            self.monster()

    def monster(self):
        new_monster = Turtle(shape="turtle")
        new_monster.color(self.random_color())
        new_monster.shape("turtle")
        new_monster.penup()
        new_monster.speed(0)
        new_monster.setheading(270)
        x = random.randint(-200, 200)
        y = random.randint(100, 250)
        new_monster.setposition(x, y)
        self.monsters.append(new_monster)

    def random_color(self):
        return random.choice(self.colors)

    def move_monsters(self):
        for monster in self.monsters:
            # Move the enemy
            x = monster.xcor()
            x += self.monster_speed
            monster.setx(x)
            # Move the enemy back and down
            if monster.xcor() > 280:
                # Move all the enemies down
                for e in self.monsters:
                    y = e.ycor()
                    y -= 30
                    e.sety(y)
                self.monster_speed *= -1
                # Change enemy direction
            if monster.xcor() < -280:
                # Move all enemies down
                for e in self.monsters:
                    y = e.ycor()
                    y -= 30
                    e.sety(y)
                self.monster_speed *= -1

    def check_collision(self, bullet, player, scoreboard, ):
        for monster in self.monsters:
            if is_collision(bullet, monster):
                scoreboard.add_point()
                monster.hideturtle()
                bullet.bullet_state = "ready"
                bullet.setposition(0, -340)
                # reset the enemy
                x = random.randint(-200, 200)
                y = random.randint(100, 250)
                monster.setposition(x, y)
                monster.showturtle()

            if is_collision(player, monster):
                scoreboard.game_over()

                player.clear()
                bullet.clear()
                monster.hideturtle()
                self.collision = True
                bullet.hideturtle()
                print("Game Over")
                break
