import drawing as d
def move_up():
    y=d.rocket_left.ycor()
    if(y<250):
        d.rocket_left.sety(y+10)
def move_down():
    y=d.rocket_left.ycor()
    if (y > -250):
        d.rocket_left.sety(y-10)


def move_rup():
    y=d.rocket_right.ycor()
    if(y<250):
        d.rocket_right.sety(y+10)
def move_rdown():
    y=d.rocket_right.ycor()
    if (y > -250):
        d.rocket_right.sety(y-10)
