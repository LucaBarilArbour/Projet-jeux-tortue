import turtle
t = turtle.Turtle()
t.color("red")
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
turtle.done()
t.forward(50)
