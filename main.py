from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# screen set up
screen = Screen()
screen.setup(width=700, height=700)
screen.bgcolor("black")
screen.title(titlestring="Snake Game")
screen.tracer(0)

# initialize classes
snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.update()
screen.listen()
screen.onkey(snake.snake_up, "Up")
screen.onkey(snake.snake_down, "Down")
screen.onkey(snake.snake_right, "Right")
screen.onkey(snake.snake_left, "Left")
game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move_snake()

    # detect collision with food
    if (snake.head.distance(food)) < 20:
        food.refresh()
        scoreboard.increase_score()
        snake.extend_snake()

    # detect collision with walls
    if snake.head.xcor() > 330 or snake.head.xcor() < -330 or snake.head.ycor() > 330 or snake.head.ycor() < -330:
        scoreboard.reset()
        snake.reset()


    # detect collision
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 15:
            scoreboard.reset()
            snake.reset()

screen.exitonclick()
