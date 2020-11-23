import turtle as t
from random import randint, choice

# Screen setup
screen = t.Screen()
screen.bgcolor("dark grey")
screen.delay(0)  # animation speed
screen.colormode(255)  # can also use t.colormode(255)

# Turtle setup
tim = t.Turtle()
tim.speed(10)  # turtle speed
tim.pensize(5)


# Generate random colour
def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return r, g, b


# Draw a square
def square(size):
    for _ in range(4):
        tim.fd(size)
        tim.lt(90)


# Draw a dashed line
def dash(num_dashes, line_length):
    dash_length = line_length / (num_dashes * 2 - 1)
    print(dash_length)
    tim.pd()
    tim.fd(dash_length)
    while tim.distance(0, 0) < line_length:
        tim.pu()
        tim.fd(dash_length)
        tim.pd()
        tim.fd(dash_length)


# Draw regular polygon
def polygon(sides):
    angle = 360 / sides
    tim.pencolor(random_color())
    tim.pu()
    tim.goto(-50, 150)
    tim.pd()
    for _ in range(sides):
        tim.fd(100)
        tim.rt(angle)


def walk():
    heading = [0, 90, 180, 270]
    tim.pensize(5)
    for _ in range(0, 1001):
        tim.pencolor(random_color())
        # direction = randint(0, 3)
        # if direction == 0:  # forward
        #     pass  # do nothing
        # elif direction == 1:  # left
        #     tim.lt(90)
        # elif direction == 2:  # right
        #     tim.rt(90)
        # else:
        #     tim.rt(180)
        tim.setheading(choice(heading))
        tim.fd(20)


def spirograph(quantity, size):
    angle = int(360 / quantity)
    tim.pensize(1)
    for _ in range(quantity):
        tim.pencolor(random_color())
        tim.circle(size)
        tim.lt(angle)


# Function calls
# ==============
# Draw a square
# square(100)

# Draw a dashed line
# dash(10, 400)

# Draw triangle .. decagon
# for i in range(3, 11):
#     polygon(i)

# Random walk
# walk()

# Draw a spirograph
spirograph(quantity=60, size=100)
spirograph(quantity=60, size=50)


# Open the screen and close it when clicked
screen.exitonclick()
