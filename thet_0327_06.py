import turtle
t=turtle.Turtle()
t.shape("turtle")

#n=int(input("원하는 n각형:"))

n=turtle.textinput("", "원하는 n각형:")
n=int(n)
for i in range(n):
    t.forward(100)
    t.left(360/n)
    
#Click하면 창 닫기
turtle.exitonclick()
    
    

