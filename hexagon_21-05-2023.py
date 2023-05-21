import turtle

# Set up the turtle screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Complex Long Art")
screen.setup(width=800, height=800)

# Create a turtle instance
artist = turtle.Turtle()
artist.speed(0)  # Fastest speed

# Set colors for the art
colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]

# Function to draw the complex long art


def draw_complex_long_art():
    length = 5
    angle = 91

    for _ in range(400):
        artist.forward(length)
        artist.right(angle)
        length += 2
        angle -= 0.5
        artist.color(colors[_ % len(colors)])


# Hide the turtle
artist.hideturtle()

# Call the function to draw the art
draw_complex_long_art()

# Exit the turtle screen when clicked
turtle.done()
