from turtle import forward as 앞으로
from turtle import backward as 뒤로
from turtle import mainloop as 그대로두세요
from turtle import left as 왼쪽
from turtle import right as 오른쪽
from turtle import penup as 그만그려
from turtle import pendown as 그려
from turtle import pensize as 굵기
from turtle import speed as 속도
from turtle import pencolor as 색
from turtle import clear as 지우기
from turtle import goto as 이동

import random
import turtle
import winsound
import multiprocessing

turtle.shape("turtle")

# 색의 종류 red, orange, yellow, green, blue, indigo, violet


def beepsound():
    winsound.Beep(random.randint(200, 1000), 200)
    return


def 랜덤색():
    색종류 = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
    색(색종류[random.randint(0,6)])


def 사각형그리기1(횟수):
    """사각형을 그리는 함수"""
    for i in range(횟수):
        beepsound()
        랜덤색()
        왼쪽(20)
        앞으로(50)
        왼쪽(90)
        앞으로(50)
        왼쪽(90)
        앞으로(50)
        왼쪽(90)
        앞으로(50)
        왼쪽(90)
    return

def 삼각원그리기(a, b):
    for i in range(a):
        beepsound()
        랜덤색()
        앞으로(b)
        왼쪽(10)
        뒤로(b*2)
        왼쪽(10)
    return



속도(10)
그만그려()
이동(0, 300)


그려()
winsound.Beep(440, 200)
삼각원그리기(20, 100)
사각형그리기1(20)

t1 = turtle.Turtle()
t1.shape('turtle')
t1.shape('turtle')
t1.pendown
t1.forward((100))
t1.right(100)

그대로두세요()