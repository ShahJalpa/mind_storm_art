import turtle

def draw_square(some_turtle):
    for i in range(1,5):
        some_turtle.forward(100)
        some_turtle.right(90)

def draw_triangle(some_tri):
    for i in range(1,4):
        some_tri.right(120)
        some_tri.forward(100)
        

def draw_art():
    window = turtle.Screen()
    window.bgcolor("white")
    #Create the turtle Brad - Draws a square
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("black")
    brad.speed(3)
    draw_square(brad)
    #Create the turtle Angie - Draw a circle
    angie = turtle.Turtle()
    angie.shape("arrow")
    angie.color("blue")
    angie.circle(100)
    #Create the turtle Trio - Draw a triangle
    trio = turtle.Turtle()
    trio.shape("classic")
    trio.color("red")
    trio.speed(3)
    draw_triangle(trio)

    window.exitonclick()

draw_art()


