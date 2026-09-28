import turtle
turtle.Screen().bgcolor("light purple")
square = turtle.Turtle()
num_sides = 4
side_lenght = 70
angle= 360.0 / num_sides
for i in range(num_sides):
    square.forward(side_lenght)
    square.right(angle)

turtle.done()