import turtle

t = turtle.Turtle()
dlouhost = 0
misto1 = 0
misto2 = 0
while True:
    t.speed(100)
    t.penup()
    t.goto(misto1, misto2)
    t.pendown()
    dlouhost += 4
    misto1 -= 2
    misto2 -= 2
    for i in range(4):
        t.forward(dlouhost)
        t.left(90)

