import turtle

# Set up the turtle
try:
    flag_turtle = turtle.Turtle()
except:
    flag_turtle = turtle.Turtle()
flag_turtle.speed(2)

# Calculate the height and width of the flag
height = 250
width = 450
stripe_height = height / 3
flag_turtle.pensize(3)

# Draw the saffron color (RGB: 255, 153, 51)
flag_turtle.penup()
flag_turtle.goto(-width / 2, height / 2)
flag_turtle.pendown()
flag_turtle.color(1, 0.6, 0.2)  # RGB values
flag_turtle.begin_fill()
for _ in range(2):
    flag_turtle.forward(width)
    flag_turtle.right(90)
    flag_turtle.forward(stripe_height)
    flag_turtle.right(90)
flag_turtle.end_fill()

# Draw the white color
flag_turtle.penup()
flag_turtle.goto(-width / 2, height / 2 - stripe_height)
flag_turtle.pendown()
flag_turtle.color("white")
flag_turtle.begin_fill()
for _ in range(2):
    flag_turtle.forward(width)
    flag_turtle.right(90)
    flag_turtle.forward(stripe_height)
    flag_turtle.right(90)
flag_turtle.end_fill()

# Draw the green color
flag_turtle.penup()
flag_turtle.goto(-width / 2, height / 2 - 2 * stripe_height)
flag_turtle.pendown()
flag_turtle.color("green")
flag_turtle.begin_fill()
for _ in range(2):
    flag_turtle.forward(width)
    flag_turtle.right(90)
    flag_turtle.forward(stripe_height)
    flag_turtle.right(90)
flag_turtle.end_fill()

# Draw the Ashoka Chakra (Navy Blue Circle) at the center
chakra_radius = stripe_height / 2
flag_turtle.penup()
flag_turtle.goto(0, -42)  # Center of the screen
flag_turtle.pendown()
flag_turtle.color("navy")
flag_turtle.pensize(3)
flag_turtle.circle(chakra_radius)

flag_turtle.color("navy")
flag_turtle.pensize(2)
for _ in range(24):
    flag_turtle.penup()
    flag_turtle.goto(0, 0)
    flag_turtle.left(360 / 24)
    flag_turtle.forward(chakra_radius/100)
    flag_turtle.pendown()
    flag_turtle.forward(chakra_radius)
    flag_turtle.penup()
    flag_turtle.backward(chakra_radius)

# Write the Independence Day message
flag_turtle.pensize(3)
flag_turtle.penup()
flag_turtle.goto(0, 150)  # Position above the flag
flag_turtle.pendown()
flag_turtle.color("black")
flag_turtle.write("Happy Independence Day!", align="center", font=("Verdana", 16, "bold"))

flag_turtle.hideturtle()

# Close the window on click
screen.exitonclick()
