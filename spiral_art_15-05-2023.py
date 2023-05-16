import turtle

# Create a turtle object
t = turtle.Turtle()

# Set the speed of the turtle
t.speed(7)

# Set the background color
turtle.bgcolor("black")

# Define a list of colors
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

# Set the initial size of the spiral
size = 10

# Function to draw a spiral pattern


def draw_spiral():
    global size
    for _ in range(100):
        color = colors[_ % len(colors)]  # Cycle through the colors
        t.color(color)
        t.forward(size)
        t.right(91)
        size += 1


# Set the starting position
t.penup()
t.goto(0, 0)
t.pendown()

# Draw the spiral pattern
draw_spiral()

# Hide the turtle
t.hideturtle()

# Exit the turtle graphics
turtle.done()
