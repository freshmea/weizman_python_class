import turtle as t


t.shape("turtle")
t.title("거북이 놀이")
# t.speed(3)
t.pensize(10)
# for i in range(10):
#     t.fd(100)
#     t.backward(100)
#     t.setheading(i*10)
t.clear()

t.pensize(1)
t.colormode(255)

def fxn(x,y):
    t.pencolor(255,0,0)
    t.goto(x,y)
    t. circle(80)
#이거 제대로 올라가는지 보자.

for i in range(3):
    t.pencolor(i*50, i*50, 0)
    t.circle(80)
    t.left(360/50)

t.onscreenclick(fxn)

t.mainloop()


