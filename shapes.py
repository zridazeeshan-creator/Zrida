
import turtle

# Create screen
screen = turtle.Screen()
screen.title("Drawing Shapes Using Turtle")
screen.bgcolor("white")
screen.setup(width=800, height=600)

# Create turtle
pen = turtle.Turtle()
pen.speed(5)
pen.pensize(3)

# Function to draw a triangle
def draw_triangle(x, y, color):
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.color("black", color)
    pen.begin_fill()

    for i in range(3):
        pen.forward(100)
        pen.left(120)

    pen.end_fill()

# Function to draw a rectangle
def draw_rectangle(x, y, color):
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.color("black", color)
    pen.begin_fill()

    for i in range(2):
        pen.forward(140)
        pen.left(90)
        pen.forward(80)
        pen.left(90)

    pen.end_fill()

# Function to draw a square
def draw_square(x, y, color):
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.color("black", color)
    pen.begin_fill()

    for i in range(4):
        pen.forward(80)
        pen.left(90)

    pen.end_fill()

# Draw triangles
draw_triangle(-300, 150, "lightblue")
draw_triangle(100, 150, "orange")
draw_triangle(-100, -150, "lightgreen")

# Draw rectangles
draw_rectangle(-250, -100, "pink")
draw_rectangle(100, -100, "yellow")

# Draw squares
draw_square(-40, 50, "purple")
draw_square(250, 100, "cyan")

# Hide turtle
pen.hideturtle()

# Keep window open
screen.mainloop()
