import turtle
height = 5
width = 5

turtle.speed(2)
turtle.penup()

for y in range(height):
    for x in range(width):
        turtle.dot()
        turtle.forward(20)
    turtle.backward(width * 20)
    turtle.right(90)
    turtle.forward(20)
    turtle.left(90)

turtle.exitonclick()