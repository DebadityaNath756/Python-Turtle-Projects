import turtle, math

t = turtle.Turtle()
t.getscreen().bgcolor("#994444")

t.speed(1000)

t.penup()
t.left(90)
t.forward(100)
t.right(90)
t.pendown()

def star(t, s):
    if s <= 10:
        pass
    else:
        for i in range(5):
            t.forward(s)
            star(t, s/3)
            t.left(216)


star(t, 360 )

turtle.done()
