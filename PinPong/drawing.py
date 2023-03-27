import turtle

window=turtle.Screen()
window.title("PinPong")
window.setup(width=1.0,height=1.0)
window.bgcolor("black")
window.tracer(2) #updates

#creating the place on which we will play
border=turtle.Turtle()
border.speed(0)
border.color('green')
border.begin_fill()
border.goto(-500,300) #upper left corner
border.goto(500,300) #upper right corner
border.goto(500,-300) #lower right
border.goto(-500,-300) #lower left
border.goto(-500,300)
border.end_fill()

#drawing the mid line(nett)
border.goto(0,300)
border.color("white")
border.setheading(270) #looking down
for i in range(25):
    if i%2==0:
        border.forward(24)
    else:
        border.up()
        border.forward(24)
        border.down()
border.hideturtle()

#drawing the rockets
#left
rocket_left=turtle.Turtle()
rocket_left.color('white')
rocket_left.shape('square')
rocket_left.shapesize(stretch_len=1,stretch_wid=5)
rocket_left.penup()
rocket_left.goto(-450,0)

#right
rocket_right=turtle.Turtle()
rocket_right.color('white')
rocket_right.shape('square')
rocket_right.shapesize(stretch_len=1,stretch_wid=5)
rocket_right.penup()
rocket_right.goto(450,0)


#creating the ball
ball=turtle.Turtle()
ball.shape('circle')
ball.speed(0)
ball.color('red')
ball.dx=-3
ball.dy=-3
ball.penup()
