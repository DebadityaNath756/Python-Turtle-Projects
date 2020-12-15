import turtle

s = input("What shape do you want to draw? \'s\' for square or \'t\' for triangle: ")
si = int(input("How many pixels big do you want the shape to be: "))

if s == 's':
    t = turtle.Turtle()
    for i in range(4):
        t.forward(si)
        t.left(90)
    turtle.done()
elif s == 't':
    t = turtle.Turtle()
    for i in range(3):
        t.forward(si)
        t.left(120)
    turtle.done()