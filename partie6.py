import turtle
ma_tortue = turtle.Turtle()
ma_tortue.color("red")
ma_tortue.width(10)

ma_tortue.left(90)
def etoille():
    for _ in range(5):
        ma_tortue.forward(50)
        ma_tortue.right(144)
    ma_tortue.penup()
    ma_tortue.forward(150)
    ma_tortue.pendown()
for _ in range(3):
    etoille()
    ma_tortue.right(120)
ma_tortue.left(90)
ma_tortue.penup()
ma_tortue.forward(150)
ma_tortue.pendown()
ma_tortue.forward(50)
turtle.done()
