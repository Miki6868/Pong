from turtle import Screen
from paddles import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.title("Pong Game")
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(0)


left_paddle = Paddle((-375, 0))
right_paddle = Paddle((370, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()

screen.onkeypress(left_paddle.move_up, "w")
screen.onkeypress(left_paddle.move_down, "s")
screen.onkeypress(right_paddle.move_up, "Up")
screen.onkeypress(right_paddle.move_down, "Down")

game_is_on = True
while game_is_on:
    screen.update()
    ball.move()
    time.sleep(ball.move_speed)
    # Detect collision with top and bottom walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    # Detect collision with paddles
    if (ball.xcor() > 350 and ball.distance(right_paddle) < 50) or (ball.xcor() < -350 and ball.distance(left_paddle) < 50): 
        ball.bounce_x()
    # Detect if ball goes out of bounds
    if ball.xcor() > 380 or ball.xcor() < -380:
        if ball.xcor() > 380:
            scoreboard.increase_player_l_score()
        else:
            scoreboard.increase_player_r_score()
        ball.reset_position()    


screen.exitonclick()