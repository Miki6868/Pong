from turtle import Screen
from paddles import Paddle


screen = Screen()
paddle = Paddle()


screen.setup(width=800, height=600)
screen.bgcolor("black")

screen.listen()
screen.onkey(paddle.go_up, "Up")
screen.onkey(paddle.go_down, "Down")


screen.exitonclick()