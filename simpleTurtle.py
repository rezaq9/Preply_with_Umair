import turtle 
from turtle import Turtle 
import random
turtles = []
colors = ['red','green','blue','yellow','orange','purple']
turtle.tracer(0,0)
for i in range(10):
    t = Turtle()
    t.color(random.choice(colors))
    t.shapesize(2,2)
    turtles.append(t)
    
for t in turtles:
    t.goto(random.randint(-200,200),random.randint(-200,200))
    for i in range (500):
        for i in range(4):
            t.forward(100)
            t.left(90)
        t.left(random.choice([10,11,12]))
    turtle.update()
    
turtle.done()
