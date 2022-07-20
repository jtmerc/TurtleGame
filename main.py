# import modules
import time
import turtle
import random

# screen
screen = turtle.Screen()
screen.bgcolor('silver')

# player 1
player_one = turtle.Turtle()
player_one.color('black')
player_one.shape('turtle')

# player 2
player_two = player_one.clone()
player_two.color('white')
player_two.shape('turtle')

# player 3
player_three = player_one.clone()
player_three.color('green')
player_three.shape('turtle')

# position players
player_one.penup()
player_one.goto(-300, 200)
player_two.penup()
player_two.goto(-300, -200)
player_three.penup()
player_three.goto(-300, 0)

# finish line
player_one.goto(300, -250)
player_one.left(90)
player_one.pendown()
player_one.color('black')
player_one.forward(500)
player_one.write('Finish!', font=30)
player_one.penup()
player_one.color('black')
player_one.goto(-300, 200)
player_one.right(90)

# Both players have 'pen' tail
player_one.pendown()
player_two.pendown()
player_three.pendown()

# Values for die
die = [1, 2, 3, 4, 5, 6]

# Creates the game
for i in range(30):
    if player_one.pos() >= (300, 250):
        print("Player One Wins!")
        break
    elif player_two.pos() >= (300, -250):
        print("Player Two Wins!")
        break
    elif player_three.pos() >= (300, 0):
        print("Player Two Wins!")
        break
    else:
        die_roll = random.choice(die)
        player_one.forward(30 * die_roll)
        time.sleep(1)
        die_roll2 = random.choice(die)
        player_two.forward(30 * die_roll)
        time.sleep(1)
        die_roll3 = random.choice(die)
        player_three.forward(30 * die_roll)
        time.sleep(1)

# two players in game - who ever gets to other side wins
turtle.done()
