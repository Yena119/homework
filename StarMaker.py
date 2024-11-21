import turtle
import random
t = turtle.Turtle()
t.shape("turtle")
turtle.colormode(255)

s = turtle.textinput("", "별의 개수는? :")
num = int(s)

for i in range(num) :
   r = random.randint(0, 255)
   g = random.randint(0, 255)
   b = random.randint(0, 255) # 별 색깔을 랜덤하게

   x = random.randrange(-300, 300)
   y = random.randrange(-300, 300) # 별 위치를 랜덤하게
# 300 이상의 범위를 설정하니까 컨버스를 벗어나버림

   t.fillcolor(r, g, b)
   t.begin_fill()
   t.penup()
   t.goto(x, y)
   t.pendown()

   j=0
   star = random.randint(30, 100) 
# 별 크기를 30에서 100사이 크기로 랜덤하게
   while j < 5:
       t.forward(star)
       t.right(144)
       j = j+1
   t.end_fill()

turtle.mainloop()
