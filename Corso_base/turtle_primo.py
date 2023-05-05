
import turtle

t=turtle.Turtle()
t.forward(50)
t.right(90)
t.forward(50)
t.right(90)
t.forward(50)
t.right(90)
t.forward(50)
t.right(90)

for i in range(0,4):
    t.forward(100)
    t.right(90)

    
passo=200
for i in range(0,4):
    t.forward(passo)
    t.right(90)

    
passo=20
for i in range(0,4):
    t.forward(passo)
    t.right(90)

    

t.color('red')
for i in range(0,4):
    t.forward(passo)
    t.right(90)

    
t.pensize(10)
for i in range(0,4):
    t.forward(passo)
    t.right(90)
for i in range(0,4):
     t.forward(passo)
     t.right(90)
 
     
t.goto(100,100)
t.pensize(4)
t.goto(100,200)
t.color('black')
t.goto(0,0)
t.speed(10)
t.goto(-100,100)
t.pensize(2)
t.circle(20)
t.circle(50)
t.circle(100)
#t.clear()
#t.penup()
#t.goto(100,200)
#turtle.bye()
