from turtle import Turtle, Screen
from random import randint

screen = Screen()
# creating turtle objects
t1 = Turtle()
t2 = Turtle()
t3 = Turtle()
t4 = Turtle()
t5 = Turtle()
t6 = Turtle()
t7 = Turtle()
t8 = Turtle()
# t8 is the final line
t_list = [t1, t2, t3, t4, t5, t6, t7]
t1.shape("turtle")
t2.shape("turtle")
t3.shape("turtle")
t4.shape("turtle")
t5.shape("turtle")
t6.shape("turtle")
t7.shape("turtle")
t8.shape("arrow")
t1.color("red")
t1.color = "red"
t2.color("blue")
t2.color = "blue"
t3.color("brown")
t3.color = "brown"
t4.color("purple")
t4.color = "purple"
t5.color("yellow")
t5.color = "yellow"
t6.color("pink")
t6.color = "pink"
t7.color("black")
t7.color = "black"
a = 0

# drawing the final line:
t8.penup()
t8.goto(200, 300)
t8.pendown()
t8.right(90)
t8.speed(1)
t8.forward(600)
t8.hideturtle()
# turtle.hide is applicable for hiding the arrow or the turtle

# establishing different turles in their places
for t in t_list:
    t.penup()
    t.speed(1)
    t.goto(-300, -200 + a)
    a = a + 70
# predicitng the winner
screen.listen()
winner = screen.textinput(" turtle competition:)",
                          "which turtle will be won?\n blue or red or pink or black or brown or ETC")

for t in t_list:
    t.walksum = 0
b = True
while b:
    for t in t_list:
        t.walkr = randint(10, 30)
        t.forward(t.walkr)
        t.walksum = t.walksum + t.walkr
        if t.walksum > 500:
            b = False
            print(f"the winner is {t.color} with {t.walksum} step")
            real_winner = t.color
            break

if real_winner == winner:
    print(f"congradulations!!!\n your guess was true\n {real_winner} was winner")
else:
    print(f"winner was {real_winner} \nyou could not guess correctly! ")
screen.exitonclick()
