import turtle
t=turtle.Turtle()

t.shape("turtle")

#정삼각형
for i in range(3):
    t.forward(100)
    t.left(360/3)
    
#이동하기
t.penup()
t.goto(200,0)
t.pendown()

#정사각형
for i in range(4):
    t.forward(100)
    t.left(360/4)
    
#Click하면 창 닫기
turtle.exitonclick()