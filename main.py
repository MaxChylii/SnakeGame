import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.tracer(0)
screen.title("Snake")

snake = Snake()
food = Food()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
scoreboard = Scoreboard()

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # detect collision with food
    if snake.head.distance(food) < 15:
        snake.extend()
        food.refresh()
        scoreboard.increase_score()

    # detect collision with wall
    if abs(snake.head.xcor()) > 290 or abs(snake.head.ycor()) > 290:
        scoreboard.reset()
        snake.reset()

    # detect collision with tail
    for segment in snake.body[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()

screen.exitonclick()
