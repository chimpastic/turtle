import turtle

# Set up the turtle screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Complex Turtle Art")
screen.setup(800, 800)

# Create a turtle instance
pen = turtle.Turtle()
pen.speed(0)  # Set the speed to the fastest

# Define the colors
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

# Function to draw a complex shape


def draw_complex_shape(size, sides):
    angle = 360 / sides
    for _ in range(sides):
        pen.forward(size)
        pen.right(angle)


# Draw the complex turtle art
for i in range(200):
    pen.color(colors[i % len(colors)])  # Switch colors
    draw_complex_shape(i, 6)  # Change the number of sides for each iteration
    pen.right(91)  # Rotate the turtle

# Hide the turtle
pen.hideturtle()

# Exit on click
turtle.done()
