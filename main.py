import time
from turtle import Turtle, Screen
import random
from snake import Snake
from food import Food
from score import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)


# for item in range(1, 4):
#     timmy = Turtle(shape="square")
#     timmy.penup()
#     timmy.color("white")
#     pos += 20
#     timmy.goto(x=0 - pos, y=0)
#     all_turtle.append(timmy)

# print(all_turtle)


snake = Snake()
food = Food()
score = Scoreboard()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)

    snake.move()
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_score()

    # Detect wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        score.reset()
        snake.reset()

    #Detect collision with the tail
    for segment in snake.all_turtle[1:]:
        # if segment == snake.head:
        #     pass
        if snake.head.distance(segment) < 10:
            score.reset()








screen.exitonclick()