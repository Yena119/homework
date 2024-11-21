import turtle
import random

t = turtle.Turtle()
t.shape("turtle")


for i in range(5):
   length = random.randint(1, 100)
   t.forward(length)
   angle = random.randint(-180, 180)
   t.right(angle)
   n = random.randint(3, 10)
   for j in range(n):
       t.forward(70)
       t.left(360/n)

turtle.mainloop()
