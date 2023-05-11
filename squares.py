import turtle
import random

# Set up the turtle screen
screen = turtle.Screen()
screen.bgcolor("black")

# Create a turtle object
art = turtle.Turtle()
art.speed(20)

# Set turtle properties
art.shape("turtle")
art.pensize(2)

# Define the colors for the pattern
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

# Draw the complicated satisfying art
for _ in range(200):
    # Randomly select a color
    color = random.choice(colors)
    art.color(color)

    # Draw a square
    for _ in range(4):
        art.forward(100)
        art.right(90)

    # Rotate the turtle by a random angle
    art.right(random.randint(1, 180))

# Hide the turtle
art.hideturtle()

# Exit the turtle graphics window
turtle.done()
