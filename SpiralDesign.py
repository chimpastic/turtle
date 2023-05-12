import turtle

# Set up the turtle screen
screen = turtle.Screen()
screen.bgcolor("black")

# Create a turtle instance
pen = turtle.Turtle()
pen.speed(0)  # Set the speed to the fastest

# Define colors
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

# Draw the spiral pattern
for i in range(360):
    pen.color(colors[i % 6])  # Select color from the list
    pen.forward(i * 2)  # Move forward
    pen.left(59)  # Turn left

# Hide the turtle
pen.hideturtle()

# Exit on click
turtle.done()
