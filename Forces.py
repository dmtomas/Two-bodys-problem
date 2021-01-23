import turtle
import math

# Variables for .
dt = 0.00000003  # This is the accuracy of the simulation (smaller is better but slower).



force = input("Enter the force you want to graph (force must be written respect to r): ")   # We define the
# interaction forces between both bodies. We recommend using a big constant, because the distance is based on the
# pixels.

# Put the screen
wn = turtle.Screen()
wn.bgcolor("black")

# Initial conditions to object 1.
m1 = 50  # Mass of the object 1.
Obj1 = turtle.Turtle()
Obj1.shape("circle")
Obj1.color("white")
Obj1.speed(0)
Obj1.dx = 30000000  # Initial velocity of the object1 x coordinate.
Obj1.dy = 0  # Initial velocity of the object1 y coordinate.
Obj1.penup()
Obj1.goto(-100, 50)  # Initial position of the object 1

# Initial conditions object 2.
m2 = 50  # Mass of the object 2.
Obj2 = turtle.Turtle()
Obj2.shape("circle")
Obj2.color("blue")
Obj2.speed(0)
Obj2.penup()
Obj2.dx = -30000000  # Initial velocity of the object2 coordinate x.
Obj2.dy = 0  # Initial velocity of the object2 coordinate y.
Obj2.goto(100, -100)  # Initial position of the object 2

# Objects draw their path
Obj1.pendown()
Obj2.pendown()


# This loop draws the trajectories. (is not in real time the simulation)
while True:
    # r is the distance between the objects.
    r = math.sqrt((Obj1.xcor() - Obj2.xcor()) ** 2 + (Obj1.ycor() - Obj2.ycor()) ** 2)

    f = eval(force)

    # Velocity variation for the objects.
    if r > 20:
        Obj1.dy -= (Obj2.ycor() - Obj1.ycor()) * f * dt / (r*m1)
        Obj1.dx -= (Obj2.xcor() - Obj1.xcor()) * f * dt / (r*m1)
        Obj2.dy += (Obj2.ycor() - Obj1.ycor()) * f * dt / (r * m2)
        Obj2.dx += (Obj2.xcor() - Obj1.xcor()) * f * dt / (r * m2)
    else:
        # If there is a collision stops.
        Obj1.dx = 0
        Obj1.dy = 0
        Obj2.dx = 0
        Obj2.dy = 0

    # Position that both objects have
    Obj2.sety(Obj2.ycor() + Obj2.dy*dt)
    Obj2.setx(Obj2.xcor() + Obj2.dx*dt)
    Obj1.sety(Obj1.ycor() + Obj1.dy*dt)
    Obj1.setx(Obj1.xcor() + Obj1.dx*dt)


wn.mainloop()
