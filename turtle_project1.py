import turtle

t = turtle.Turtle()

t.speed(1)

t.speed(5)

t.showturtle()

t.color("#99E64C")
t.fillcolor("#CC66FF")

t.hideturtle()

for i in range(4):

    t.begin_fill()
    t.forward(100)
    t.right(90)
    t.forward(100)
    t.right(90)
    t.forward(100)
    t.right(90)
    t.forward(100)

    t.end_fill()

    t.penup()
    t.forward(10)
    t.pendown()



turtle.done()