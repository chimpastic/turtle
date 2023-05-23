import turtle

# Setup
screen = turtle.Screen()
screen.bgcolor("black")
pen = turtle.Turtle()
pen.speed(0)
pen.pensize(2)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

# Art
for _ in range(1000):
    pen.color(colors[_ % len(colors)])
    pen.forward(_)
    pen.right(59)

# Hide the turtle
pen.hideturtle()

# Exit on click
turtle.done()
