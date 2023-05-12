import turtle
import random

# Set up the turtle screen
screen = turtle.Screen()
screen.bgcolor("black")

# Create a turtle object
art = turtle.Turtle()
art.speed(0)

# Set turtle properties
art.shape("turtle")
art.pensize(2)

# Define the colors for the pattern
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

# Draw the complex turtle art
for _ in range(200):
    # Randomly select a color
    color = random.choice(colors)
    art.color(color)

    # Draw a circle
    art.circle(100)

    # Rotate the turtle by a random angle
    art.right(random.randint(1, 360))

# Hide the turtle
art.hideturtle()

# Exit the turtle graphics window
turtle.done()
