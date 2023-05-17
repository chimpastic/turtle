import json
import turtle

with open('geoBoundaries-IND-ADM0_simplified.geojson') as file:
    data = json.load(file)


co = (data['features'][0]['geometry']['coordinates'])
print(co)
# Create a turtle object
print(len(co[0][0]))

print(co[0][0][-1])
t = turtle.Turtle()

# Set the speed of the turtle
t.speed(1)


# Set the background color
turtle.bgcolor("black")

# Set the pen color and fill color
t.color("white")
screen = turtle.Screen()
screen.setup(320, 480)
# Define the coordinates for each continent
# for i in [[0, 0], [0, 1], [1, 1], [1, 0]]
cord_x = []
cord_y = []
for i in co:
    for j in i:
        for k in j:
            cord_x.append(k[0])
            cord_y.append(k[1])
max_cord_x = max(cord_x)
min_cord_x = min(cord_x)
max_cord_y = max(cord_y)
min_cord_y = min(cord_y)
len(co[0])
cot = {}
c = 0
for d in co:
    cot[c] = [[270*((i[0]-min_cord_x)/(max_cord_x-min_cord_x)), 480 *
               ((i[1]-min_cord_y)/(max_cord_y-min_cord_y))-40] for i in d[0]]
    c += 1
continents = {
    "Asia": [[1080*((i[0]-min_cord_x)/(max_cord_x-min_cord_x)), 1920*((i[1]-min_cord_y)/(max_cord_y-min_cord_y))] for i in co[1][0]]
}

print(cot.keys())

# Draw the continents
for continent, coordinates in cot.items():
    t.penup()
    t.goto(coordinates[0])
    t.pendown()
    t.fillcolor('orange')
    t.begin_fill()
    for coord in coordinates[1:]:
        t.goto(coord)
    t.goto(coordinates[0])
    t.end_fill()

# Hide the turtle
t.hideturtle()
print(max_cord_x, max_cord_y, min_cord_x, min_cord_y)
print(240*6*((6.8-min_cord_y)/(max_cord_y-min_cord_y)))
print(len(co))
# Exit the turtle graphics
turtle.done()
