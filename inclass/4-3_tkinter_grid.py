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

# import tkinter as tk
#
# root = tk.Tk()
# root.geometry('600x600')
# root.resizable(False, False)
# image = tk.PhotoImage(file="../icon/dot_red.gif")
# bt=[]
# k=0
# for i in range(10):
#     for j in range(10):
#         bt.append(tk.Button(text='버튼'+str(k)))
#         a=tk.Label(image=image)
#         bt[k].place(x=55*i, y=55*j)
#         a.place(x=55*i, y=55*j+30)
#         k += 1
#
# root.mainloop()


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

import tkinter
import tkinter.font

# root=tkinter.Tk()
#
# font=tkinter.font.Font(family="맑은 고딕", size=20, slant="italic")
# print(tkinter.font.families())
# label=tkinter.Label(root, text="파이썬 3.6", font=font)
# label.pack()
#
# root.mainloop()

import tkinter as tk
from tkinter import messagebox

price={'coffee': 3500, 'latte': 4000, "smoothie": 4500, 'tea': 3000}
order = []
sum = 0

def center(toplevel):
    toplevel.update_idletasks()
    w = toplevel.winfo_screenwidth()
    h = toplevel.winfo_screenheight()
    size=tuple(int(_) for _ in toplevel.geometry().split('+')[0].split('x'))
