# import tkinter as tk
#
# root = tk.Tk()
# root.title("그리드 연습")
# root.geometry("640x400+100+100")
# root.resizable(False, False)
#
# b1 = tk.Button(root, text="(0, 0)")
# b2 = tk.Button(root, text="(0, 1)", width=20)
# b3 = tk.Button(root, text="(0, 2)")
#
# b4 = tk.Button(root, text="(1, 0)")
# b5 = tk.Button(root, text="(1, 1)")
# b6 = tk.Button(root, text="(1, 3)")
#
# b7 = tk.Button(root, text="(2, 1)")
# b8 = tk.Button(root, text="(2, 2)")
# b9 = tk.Button(root, text="(2, 4)")
#
# b1.grid(row=0, column=0)
# b2.grid(row=0, column=1)
# b3.grid(row=0, column=2)
#
# b4.grid(row=1, column=0, rowspan=2)
# b5.grid(row=1, column=1, columnspan=3)
# b6.grid(row=1, column=3)
#
# b7.grid(row=2, column=1, sticky="w")
# b8.grid(row=2, column=2)
# b9.grid(row=2, column=99)
#
# root.mainloop()


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
    bt[randk].config(bg='white')
    bt[randk].config(command=cls)
    randk = random.randint(0, 100)
    bt[randk].config(bg='blue', command=btcl)
    if time.time() - timetemp < 1:
        score += 1
        label1.config(text='성공!!  점수: '+str(score), font=f2)
    else:
        label1.config(text='실패!!  점수: '+str(score), font=f2)
    timetemp = time.time()


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

# import tkinter as tk
#
# root = tk.Tk()
# root.title("아이콘 연습")
# root.geometry("640x400+100+100")
# root.resizable(True, True)
#
# image = tk.PhotoImage(file="../icon/dot_red.gif")
#
# label = tk.Label(root, image=image)
# label.pack()
#
# root.mainloop()

# import tkinter as tk
# import tkinter.font as f
#
# root=tk.Tk()
#
# font=f.Font(family="맑은 고딕", size=20, slant="italic")
# print(f.families())
# label=tk.Label(root, text="파이썬 3.6", font=font)
# label.pack()
#
# root.mainloop()
