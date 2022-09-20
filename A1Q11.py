#Question 11

import turtle
turtle.home()

xcenter = input ("Enter x coordinate for the center of the rectangle: ")
ycenter = input ("Enter y coordinate for the center of the rectangle: ")
width= input ("Enter the width of the rectangle: ")
height = input ("Enter the height of the rectangle: ")

xcenter= float(xcenter)
ycenter = float(ycenter)
width= float(width)
height = float(height)

w2 = width / 2
h2 = height / 2
w2 = int(w2)
h2 = int(h2)

startingx = xcenter - w2
startingy = ycenter - h2 

turtle.penup()
turtle.goto(startingx, startingy)
turtle.pendown()

x1 = startingx + width
turtle.goto(x1, startingy)
y1 = startingy + height

turtle.goto(x1, y1)
turtle.goto(startingx, y1)
turtle.goto(startingx, startingy)
turtle.hideturtle()



