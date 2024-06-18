import time
from turtle import Turtle, Screen
from snake import Snake
from food import Food
import score

screen = Screen()
screen.tracer(0)
screen.setup(600, 600)
screen.bgcolor('black')
snake = Snake()
snake.create()
screen.update()
food = Food()


screen.listen()
scoreboard = score.Scoreboard()
screen.onkeypress(snake.up, 'Up')
screen.onkeypress(snake.left, 'Left')
screen.onkeypress(snake.right, 'Right')
screen.onkeypress(snake.down, 'Down')


game_is_on = True
no_coll_self = True
while game_is_on and no_coll_self:
    screen.update()
    time.sleep(0.1)
    snake.link_segments()
    head = (snake.head.xcor(), snake.head.ycor())
    if snake.head.distance(food) < 11:
        food.vanish()
        snake.extend()
        scoreboard.add_score()
    game_is_on = snake.collision_with_wall()
    segments = snake.all_segments[2:]
    for _ in segments:
        if snake.head.distance(_) < 12:
            no_coll_self = False
    if not game_is_on or not no_coll_self:
        food.game_over()
        snake.game_over()
        scoreboard.game_over()


screen.exitonclick()
