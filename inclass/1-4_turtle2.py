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
from turtle import circle as 원

import random
import turtle
turtle.shape("turtle")
import winsound

# 색의 종류 red, orange, yellow, green, blue, indigo, violet
def 사각형():
    앞으로(100)
    왼쪽(90)
    앞으로(100)
    왼쪽(90)
    앞으로(100)
    왼쪽(90)
    앞으로(100)
    return
# winsound.Beep(500, 2000)
# for i in range(10):
#     사각형()
#     왼쪽(10)
def 고사각형(a, b):
    turtle.goto(a, b)
    사각형()
    return



원(100)
사각형()
turtle.onscreenclick(고사각형)
그대로두세요()
