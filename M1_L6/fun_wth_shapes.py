import turtle
import random

# Setup screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Fun with Turtle Shapes")

t = turtle.Turtle()
t.speed(0)
t.width(2)

colors = ["red", "yellow", "blue", "green", "purple", "orange", "cyan", "white"]

def draw_polygon(sides, size):
    angle = 360 / sides
    t.color(random.choice(colors))
    for _ in range(sides):
        t.forward(size)
        t.right(angle)

# Draw multiple random shapes
for _ in range(30):
    t.penup()
    t.goto(random.randint(-300, 300), random.randint(-250, 250))
    t.pendown()
    sides = random.randint(3, 8)     # triangle to octagon
    size = random.randint(30, 100)
    draw_polygon(sides, size)

# Fun spiral
t.penup()
t.goto(0, 0)
t.pendown()
t.color("cyan")

for i in range(100):
    t.forward(i * 3)
    t.right(45)

t.hideturtle()
screen.mainloop()
