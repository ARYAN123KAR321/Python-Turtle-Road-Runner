import turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

class Player:
    def __init__(self):
        self.player = turtle.Turtle()
        self.player.shape("turtle")
        self.player.penup()
        self.player.goto(STARTING_POSITION)
        self.player.setheading(90)

    def move_up(self):
        if self.player.ycor() < FINISH_LINE_Y:
            self.player.sety(self.player.ycor() + MOVE_DISTANCE)

    def reset_position(self):
        self.player.goto(STARTING_POSITION)