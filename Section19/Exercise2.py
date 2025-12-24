from turtle import Turtle, Screen
import random

tim = Turtle()
screen = Screen()
width = 800
height = 600
start_y = -(0.5 * height) + 20
screen.setup(width=width, height=height, startx=-(0.5*width), starty=-(0.5*height))

try:
    num_turtles = int(screen.textinput(title="Welcome to Turtle Racer", prompt="How many turtles to race?"))
    if num_turtles > 10:
        num_turtles = 10
except ValueError:
    num_turtles = 6

span = height / num_turtles
y_starting_positions = [start_y + int(i*span) for i in range(num_turtles)]
x_starting_position = -(0.5 * width) + 20

try:
    user_choice = screen.textinput(title="Make your bet", prompt=f"What cokour turtle will win?").lower()
except AttributeError:
    user_choice = "red"


def random_colour_generator():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

def create_turtles(num_turltes):
    turtles = [Turtle(shape="turtle") for i in range(num_turltes)]
    return turtles

def place_turtles(turtles):
    for index, turtle in enumerate(turtles):
        turtle.penup()
        turtle.goto(x=x_starting_position, y=y_starting_positions[index])

turtles = create_turtles(num_turtles)
place_turtles(turtles)
screen.exitonclick()
