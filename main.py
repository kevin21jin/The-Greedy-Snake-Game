import turtle
from random import randrange
import copy
from time import sleep

snake = [[0, 0], [0, 10], [0, 20], [0, 30], [0, 40]]
direction = [0, 10]
food = [randrange(-20, 20) * 10, randrange(-20, 20) * 10]


def fill(x, y, color, size):
    turtle.up()
    turtle.down()
    turtle.goto(x, y)
    turtle.color(color)
    turtle.begin_fill()
    for n in range(4):
        turtle.forward(size)
        turtle.right(90)
    turtle.end_fill()


def turn(x, y):
    direction[0] = x
    direction[1] = y


def inside(head):
    return -250 < head[0] < 230 and -230 < head[1] < 250


def inbody(head):
    for i in range(len(snake) - 1):
        if head == snake[i]:
            return True
    return False


def move():
    global snake, direction, food
    head = copy.deepcopy(snake[-1])
    head = [head[0] + direction[0], head[1] + direction[1]]
    snake.append(head)

    if head == food:
        food[0] = randrange(-20, 20) * 10
        food[1] = randrange(-20, 20) * 10
    else:
        snake.pop(0)

    if not inside(head) or inbody(head):
        fill(head[0], head[1], 'red', 10)
        turtle.update()
        sleep(1.5)
        snake = [[0, 0], [0, 10], [0, 20], [0, 30], [0, 40]]
        direction = [0, 10]
        food = [randrange(-20, 20) * 10, randrange(-20, 20) * 10]

    turtle.clear()
    fill(food[0], food[1], 'pink', 10)
    for body in snake:
        fill(body[0], body[1], 'black', 10)
    turtle.update()
    turtle.ontimer(move, 100)


turtle.Screen().setup(500, 500)
turtle.tracer(0)
turtle.hideturtle()
turtle.listen()
turtle.onkey(lambda: turn(0, 10), "Up")
turtle.onkey(lambda: turn(0, -10), "Down")
turtle.onkey(lambda: turn(-10, 0), "Left")
turtle.onkey(lambda: turn(10, 0), "Right")
move()
turtle.done()
