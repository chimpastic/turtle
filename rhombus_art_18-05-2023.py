import turtle

# Set up the turtle screen
screen = turtle.Screen()
screen.bgcolor("black")

# Create a turtle object
pen = turtle.Turtle()
pen.speed(0)  # Set the speed to the fastest

# Set up colors
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

# Draw the satisfying art pattern
for _ in range(36):
    for color in colors:
        pen.color(color)
        pen.forward(100)
        pen.right(60)
        pen.forward(100)
        pen.right(120)
        pen.forward(100)
        pen.right(60)
        pen.forward(100)
        pen.right(120)

    pen.right(10)

    # Draw a rhombus in the center
    pen.color("white")
    pen.forward(50)
    pen.right(60)
    pen.forward(70)
    pen.right(120)
    pen.forward(70)
    pen.right(60)
    pen.forward(70)
    pen.right(120)
    pen.forward(50)
    pen.right(180)

# Hide the turtle
pen.hideturtle()

# Exit on click
turtle.done()
