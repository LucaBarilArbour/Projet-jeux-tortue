#!/opt/homebrew/bin/python3 
import turtle
t = turtle.Turtle()
t.width(10)

t.left(180)
def lune():
    t.color("red")
    t.fillcolor("red")
    t.begin_fill()
    t.circle(100)
    t.end_fill()


def etoille():
    t.color("yellow")
    for _ in range(5):
        t.forward(50)
        t.right(144)
    t.penup()
    t.forward(150)
    t.pendown()


t.speed(1)
lune()
etoille()
turtle.done()
