from turtle import *

#we want to paint a house

#step 1:   draw a square

width(10)
speed(40)
color("brown")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

#end of square


#drawing a door

forward(55)
color("black")
begin_fill()
left(90)
forward(100)           #hight of door

right(90)
forward(45)

right(90)
forward(100)
end_fill()


penup()
goto(200, 200)
pendown()

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

penup()
goto(170, 170)
pendown()

color("brown")
left(30)
forward(40)

right(90)
forward(40)

right(90)
forward(40)

right(90)
forward(40)

right(90)
forward(20)

width(5)
right(90)
forward(40)

right(90)
forward(20)

right(90)
forward(20)

right(90)
forward(40)

penup()
goto(40, 170)
pendown()

width(10)
left(90)
forward(40)

right(90)
forward(40)

right(90)
forward(40)

right(90)
forward(40)

width(5)
right(90)
forward(20)

right(90)
forward(40)

right(90)
forward(20)

right(90)
forward(20)

right(90)
forward(40)






exitonclick()