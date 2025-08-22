#!/opt/homebrew/bin/python3 
import turtle
t = turtle.Turtle()
t.color("yellow")
t.width(10)

t.left(90)
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
t.color("black")

for _ in range(4):
    t.forward(50)
    t.backward(50)
    t.right(20)

turtle.done()
