import turtle

if __name__ == '__main__':
    window = turtle.Screen()
    window.bgcolor('white')

    # This code makes a new Turtle. Pick a new name for the turtle
    Oliver = turtle.Turtle()

    # Make your turtle's shape 'turtle', .shape('turtle')
    Oliver.shape ('turtle')
    # Set your turtle's speed using .speed(2)
    Oliver.speed(2)

    # Set your turtle's color using .color('green') and .pencolor('blue')
    Oliver.color('green')
    Oliver.pencolor('blue')
    # Move your turtle forward using .forward(100)

    # TEST    Did your turtle move forward?

    # Move your turtle left or right using .left(90) or .right(90)
    for i in range(4):
        Oliver.forward(100)
        Oliver.left(90)
    # Now put the forward and left/right code into a for loop to repeat 4 times.
    # TEST    Did your turtle draw a square?

    # Move your turtle to a new place on the screen using .goto(x, y)
    Oliver.goto(50,50)
    # x=0 and y=0 is the center of the screen

    # Have your turtle draw a circle using .circle(radius, steps=30)
    # TEST    Did your turtle draw a circle?
    Oliver.begin_fill()
    Oliver.circle(100,360)
    Oliver.end_fill()

    # Add color to your shape by adding .begin_fill() before drawing the circle
    # and .end_fill() below
    Oliver.goto(200,200)
    # Draw 3 more shapes with different fill colors!
    Oliver.begin_fill()
    for i in range (3):
        Oliver.color('yellow')
        Oliver.forward(100)
        Oliver.left(120)
    Oliver.end_fill()

    Oliver.goto(-20,-300)

    Oliver.begin_fill()
    for i in range (6):
        Oliver.color('purple')
        Oliver.forward(100)
        Oliver.left(60)
    Oliver.end_fill()

    Oliver.goto(-300,0)

    Oliver.begin_fill()
    for i in range (5):
        Oliver.color('red')
        Oliver.forward(100)
        Oliver.left(70)
    Oliver.end_fill()


    # ===================== DO NOT EDIT THE CODE BELOW ============================
    turtle.done()
