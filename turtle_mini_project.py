import turtle


def draw_j():
    letter_j = turtle.Turtle()
    letter_j.color("white")
    letter_j.setposition(0, 0)
    letter_j.right(90)
    letter_j.forward(100)
    letter_j.right(90)
    letter_j.forward(50)


def draw_e():
    letter_e = turtle.Turtle()
    letter_e.up()
    letter_e.setposition(30, 0)
    letter_e.down()
    letter_e.color("white")
    letter_e.right(90)
    letter_e.forward(100)
    letter_e.left(90)
    e_arm_y_coordinates = [0, -50, -100]
    for each in e_arm_y_coordinates:
        letter_e.up()
        letter_e.setposition(30, each)
        letter_e.down()
        letter_e.forward(50)


def draw_m():
    letter_m = turtle.Turtle()
    letter_m.color("white")
    letter_m.up()
    letter_m.setposition(110, -100)
    letter_m.down()
    letter_m.left(90)
    letter_m.forward(100)
    letter_m.right(135)
    letter_m.forward(40)
    letter_m.left(90)
    letter_m.forward(40)
    letter_m.right(135)
    letter_m.forward(100)


def draw_initials():
    window = turtle.Screen()
    window.bgcolor("lightblue")
    draw_j()
    draw_e()
    draw_m()
    window.exitonclick()

draw_initials()
