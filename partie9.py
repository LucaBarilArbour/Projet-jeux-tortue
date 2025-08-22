#!/opt/homebrew/bin/python3 
import turtle
t = turtle.Turtle()
t.color("yellow")
t.width(10)

t.left(90)
def lune():
    t.color("grey")
    t.fillcolor("grey")
    t.begin_fill()
    t.circle(100)
    t.end_fill()
    t.left(90)
    t.forward(50)
    t.right(90)
    t.forward(50)
    t.left(90)
    t.color("white")
    t.fillcolor("white")
    t.begin_fill()
    t.speed(1)
    t.circle(100)
    t.end_fill()


def etoille():
    for _ in range(5):
        t.forward(50)
        t.right(144)
    t.penup()
    t.forward(150)
    t.pendown()

for _ in range(3):
    etoille()
    t.right(120)

t.left(90)
t.penup()
t.forward(150)
t.pendown()

lune()
turtle.done()
