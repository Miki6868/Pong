from turtle import Screen
from paddles import Paddle

<<<<<<< HEAD

screen = Screen()
paddle = Paddle()


screen.setup(width=800, height=600)
screen.bgcolor("black")

screen.listen()
screen.onkey(paddle.go_up, "Up")
screen.onkey(paddle.go_down, "Down")
=======
screen = Screen()
screen.title("Pong Game")
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(0)


left_paddle = Paddle((-390, 0))
right_paddle = Paddle((380, 0))

screen.listen()

screen.onkeypress(left_paddle.move_up, "w")
screen.onkeypress(left_paddle.move_down, "s")
screen.onkeypress(right_paddle.move_up, "Up")
screen.onkeypress(right_paddle.move_down, "Down")

game_is_on = True
while game_is_on:
    screen.update()
>>>>>>> c2f1b67 (main and paddles ,paddles onkeypress works better)


screen.exitonclick()