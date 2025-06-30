from turtle import Turtle,Screen
import random

def starting_line(y,t):
    t.penup()
    t.goto(-230,y)
user_bet = False
win = False
found_winner = False
winner_color = ""
screen = Screen()
screen.setup(width=500,height=400)
bet = screen.textinput(title="Make a choice", prompt="Which turtle wins?")
t1 =Turtle(shape="turtle")
t2 =Turtle(shape="turtle")
t3 =Turtle(shape="turtle")
t4 =Turtle(shape="turtle")
t5 =Turtle(shape="turtle")
t6 =Turtle(shape="turtle")

t1.color("red")
t2.color("green")
t3.color("orange")
t4.color("blue")
t5.color("yellow")
t6.color("black")

turtle_list = [t1,t2,t3,t4,t5,t6]

if bet:
    user_bet = True

while user_bet:
    starting_line(20, t1)
    starting_line(60, t2)
    starting_line(100, t3)
    starting_line(-20, t4)
    starting_line(-60, t5)
    starting_line(-100, t6)
    while not found_winner:
        for turtle in turtle_list:
            new_x = random.randint(0,10)
            x = turtle.xcor()
            if x+new_x >= 230:
                new_x = 230 - x
                winner_color = turtle.color()
                winner_color = winner_color[0]
                found_winner = True
                if bet == winner_color:
                    win = True
            turtle.forward(new_x)

    if win:
        print("You Won!!!")
    else:
        print(f"winner is {winner_color}, you have LOST!!!!")
    user_bet = False

screen.exitonclick()
