import turtle
import drawing as d
import control as c
from random import choice, randint



#count the score
FONT=("Arial",44)
score_right=0
score1=turtle.Turtle(visible=False)
score1.color('white')
score1.penup()
score1.setposition(-200,300)
score1.write(score_right,font=FONT)

score_left=0
score2=turtle.Turtle(visible=False)
score2.color('white')
score2.penup()
score2.setposition(200,300)
score2.write(score_left,font=FONT)

d.window.listen()
d.window.onkeypress(c.move_up,"w")
d.window.onkeypress(c.move_down,"s")



d.window.listen()
d.window.onkeypress(c.move_rup,"8")
d.window.onkeypress(c.move_rdown,"2")


#making the ball bounce the bounds
while True:
    d.window.update()
    d.ball.setx(d.ball.xcor()+d.ball.dx)
    d.ball.sety(d.ball.ycor() + d.ball.dy)
    if d.ball.ycor()>=290:
        d.ball.dy=-d.ball.dy
    if d.ball.ycor()<=-290:
        d.ball.dy=-d.ball.dy

    if d.ball.xcor()>=490:
        score_left+=1
        score1.clear()
        score1.write(score_left,font=FONT)
        d.ball.goto(0,randint(-150,150))
        d.ball.dx = choice([-1, 1])
        d.ball.dy = choice([-1, 1])
    if d.ball.xcor()<=-490:
        score_right+=1
        score2.clear()
        score2.write(score_right, font=FONT)
        d.ball.goto(0,randint(-150,150))
        d.ball.dx = choice([-1, 1])
        d.ball.dy = choice([-1, 1])
    if d.ball.ycor()>=d.rocket_right.ycor()-50 and \
        d.ball.ycor()<=d.rocket_right.ycor()+50 \
        and d.ball.xcor()>=d.rocket_right.xcor()-5\
        and d.ball.xcor()<=d.rocket_right.xcor()+5:
        d.ball.dx=-d.ball.dx
    if d.ball.ycor()>=d.rocket_left.ycor()-50 and \
        d.ball.ycor()<=d.rocket_left.ycor()+50 \
        and d.ball.xcor()>=d.rocket_left.xcor()-5\
        and d.ball.xcor()<=d.rocket_left.xcor()+5:
        d.ball.dx=-d.ball.dx

# window.mainloop()
# window.exitonclick()