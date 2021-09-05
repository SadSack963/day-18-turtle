import turtle
from turtle import Turtle, Screen

colors = ["silver", "red", "yellow", "green", "blue", "cyan", "white",]
_shapes = {
    "arrow": ((-10, 0), (10, 0), (0, 10)),
    "turtle": ((0, 16), (-2, 14), (-1, 10), (-4, 7),
               (-7, 9), (-9, 8), (-6, 5), (-7, 1), (-5, -3), (-8, -6),
               (-6, -8), (-4, -5), (0, -7), (4, -5), (6, -8), (8, -6),
               (5, -3), (7, 1), (6, 5), (9, 8), (7, 9), (4, 7), (1, 10),
               (2, 14)),
    "circle": ((10, 0), (9.51, 3.09), (8.09, 5.88),
               (5.88, 8.09), (3.09, 9.51), (0, 10), (-3.09, 9.51),
               (-5.88, 8.09), (-8.09, 5.88), (-9.51, 3.09), (-10, 0),
               (-9.51, -3.09), (-8.09, -5.88), (-5.88, -8.09),
               (-3.09, -9.51), (-0.00, -10.00), (3.09, -9.51),
               (5.88, -8.09), (8.09, -5.88), (9.51, -3.09)),
    "square": ((10, -10), (10, 10), (-10, 10),
               (-10, -10)),
    "triangle": ((10, -5.77), (0, 11.55),
                 (-10, -5.77)),
    "classic": ((0, 0), (-5, -9), (0, -7), (5, -9)),
    "fighter": ((0, 5), (-5, 0), (-10, 10), (-5, -10), (0, 0), (5, -10), (10, 10), (5, 0), (0, 5))
}

screen = Screen()
screen.setup(width=700, height=400)
screen.bgcolor("black")
turtle.addshape('fighter', _shapes['fighter'])

# turtle.register_shape('my_shape', ((0, 5), (-5, 0), (-10, 10), (-5, -10), (5, -10), (10, 10), (5, 0), (0, 5)))
# tim = Turtle(shape='my_shape')

i = 0
for shape in _shapes:
    tim = Turtle(shape=shape)
    tim.color(colors[i])
    tim.speed(1)
    i += 1
    tim.pu()
    for item in _shapes[shape]:
        # print(f'{item = }')
        x = item[0] * 10
        y = item[1] * 10
        tim.goto(x, y)
        tim.pd()
    tim.goto(_shapes[shape][0][0] * 10, _shapes[shape][0][1] * 10)
    tim.hideturtle()
screen.exitonclick()
