# from turtle import Turtle, Screen
# from snake import Snake
# import time
# new_segment=Turtle()
# screen=Screen()
# screen.setup(height=600, width=600)
# screen.title("welcome to my snake game😎😎 ")
# screen.bgcolor("black")
# screen.tracer(0)
#
# snake =Snake()
# screen.listen()
# screen.onkey(snake.up, "Up")
# screen.onkey(snake.down,"Down")
# screen.onkey(snake.left,"Left")
# screen.onkey(snake.right,"Right")
# is_segment_on=True
# while is_segment_on:
#     screen.update()
#     time.sleep(0.2)
#     snake.move()
#
#
#
#
#
#
#
# # tim.color("white")
# # # tim.fillcolor("blue")
# # tim.begin_fill()
# # for x in range(4):
# #     tim.back(20)
# #     tim.left(90)
# # for y in range(4):
# #     tim.forward(20)
# #     tim.right(90)
# # tim.forward(20)
# # for y in range(4):
# #     tim.forward(20)
# #     tim.right(90)
# # tim.end_fill()
#
# # for x in range(4):
# #     tim.forward(20)
# #     tim.left(90)
#
#
# screen.exitonclick()

from turtle import Screen
from score import Score_board
from snake import Snake
import time
from food import Food
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("welcome to the Snake Game made by Andre 😎" "here we go for fun 😁😁😁 ")
screen.tracer(0)

snake = Snake()
food = Food()
score=Score_board()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.3)
    snake.move()
#         check for collision with the food
    if snake.head.distance(food)<15:
        food.refresh()
        snake.extend_snake_size()
        score.score_mark()

        # check for collision with the wall
    if snake.head.xcor()>280 or snake.head.ycor()<-280 or snake.head.xcor()<-280 or snake.head.ycor()>280:
        score.reset()
        snake.reset()
    # ? detection for collision with the tail
    for segment in snake.segments[1:]:
        if segment==snake.head:
            pass
        elif snake.head.distance(segment)<10:
            score.reset()
            snake.reset()

screen.exitonclick()
