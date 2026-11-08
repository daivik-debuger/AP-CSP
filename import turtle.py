import turtle

window = turtle.Screen()
window.title("Raspberry Pi")
window.bgcolor("#F5F5F5")

pen = turtle.Turtle()
pen.speed(5)
pen.pensize(4)

def draw_druplet(x, y, radius):
    pen.penup()
    pen.goto(x, y - radius)
    pen.pendown()
    pen.color("#8B0032", "#C51A4A")
    pen.begin_fill()
    pen.circle(radius)
    pen.end_fill()

draw_druplet(0, -90, 35)
draw_druplet(-45, -60, 32)
draw_druplet(45, -60, 32)
draw_druplet(-65, -15, 30)
draw_druplet(65, -15, 30)
draw_druplet(-40, 30, 28)
draw_druplet(40, 30, 28)
draw_druplet(0, 0, 32)
draw_druplet(0, -45, 32)

def draw_leaf(start_x, start_y, heading, angle, direction):
    pen.penup()
    pen.goto(start_x, start_y)
    pen.pendown()
    pen.color("#004225", "#87A922")
    pen.setheading(heading)
    pen.begin_fill()
    pen.circle(direction * 70, angle)
    pen.left(direction * (180 - angle))
    pen.circle(direction * 70, angle)
    pen.end_fill()

draw_leaf(-5, 55, 45, 95, 1)
draw_leaf(5, 55, 135, 95, -1)

pen.hideturtle()
window.exitonclick()
