import turtle

# Set up the turtle screen
screen = turtle.Screen()
screen.bgcolor("black")

# Create a turtle instance
artist = turtle.Turtle()
artist.speed(0)  # Set the speed to the fastest

# Define colors
colors = ["red", "blue", "green", "yellow", "orange", "purple"]

# Draw the complex art
for i in range(200):
    artist.pencolor(colors[i % len(colors)])  # Cycle through the colors
    artist.width(i / 100 + 1)  # Increase the width of the pen
    artist.forward(i)
    artist.left(59.4)

    # Add a nested loop for additional complexity
    for j in range(6):
        artist.pencolor(colors[j % len(colors)])  # Cycle through the colors
        artist.width(j / 100 + 1)  # Increase the width of the pen
        artist.forward(j)
        artist.left(59.4)

# Exit on click
turtle.done()
