"""
간단한 버튼 게임
"""

import tkinter as tk
import tkinter.font as f
import random
import time

root = tk.Tk()
root.geometry('600x600')
root.resizable(False, False)

timetemp = time.time()
f2 = f.Font(family="맑은 고딕", size=20, slant="italic")
randk = 0
score = 0


def btcl():
    global score
    global randk
    global timetemp

    #이번 버튼 초기화
    bt[randk].config(bg='white')
    bt[randk].config(command=cls)

    #시간계산과 성공실패 출력
    if time.time() - timetemp < 1:
        score += 1
        label1.config(text='성공!!  점수: '+str(score), font=f2)
    else:
        label1.config(text='실패!!  점수: '+str(score), font=f2)
    timetemp = time.time()

    # 새로운 버튼 만듬
    randk = random.randint(0, 100)
    bt[randk].config(bg='blue', command=btcl)


def cls():
    pass



bt = []
k = 0
for i in range(10):
    for j in range(10):
        bt.append(tk.Button(text='버튼' + str(k)))
        bt[k].place(x=55 * i, y=55 * j)
        k += 1

label1 = tk.Label(text='메세지')
label1.place(x=100, y=550)

btcl()

root.mainloop()