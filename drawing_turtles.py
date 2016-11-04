import turtle  # used to draw in Python
# my final code is slightly different than the video answer, but produces
# the same output

def draw_square_circle_and_triangle():
    window = turtle.Screen()
    window.bgcolor("lightblue")
    
    brad = turtle.Turtle()  # grab a turtle
    brad.shape("turtle")
    brad.color("white")
    brad.speed(4)
    brad.width(2)

    for i in range (1,37):
        square_side = 1
        number_of_sides_in_square = 4
        while square_side <= number_of_sides_in_square:
            brad.forward(100)
            brad.right(90)
            square_side += 1

        brad.right(10)

    """angie = turtle.Turtle()
    angie.shape("arrow")
    angie.color("blue")
    angie.circle(100)

    thomas = turtle.Turtle()
    thomas.shape("circle")
    thomas.color("black")

    triangle_side = 1
    number_of_sides_in_triangle = 3
    while triangle_side <= number_of_sides_in_triangle:
        thomas.forward(200)
        thomas.right(120)
        triangle_side += 1"""

    window.exitonclick()

draw_square_circle_and_triangle()