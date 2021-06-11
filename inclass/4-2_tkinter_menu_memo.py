from tkinter import *
import os
from tkinter.filedialog import *

es = ""


def newFile():
    top.title("제목없음- 메모장")
    file = None
    ta.delete(1.0, END)


def openFile():
    file = askopenfilename(title="파일 선택", filetypes=(("텍스트 파일", "*.txt"), ("모든 파일", "*.*")))
    top.title(os.path.basename(file) + " - 메모장")
    ta.delete(1.0, END)
    f = open(file, "r")
    ta.insert(1.0, f.read())
    f.close()


def saveFile():
    f = asksaveasfile(mode="w", defaultextension=".txt")
    if f is None:
        return
    ts = str(ta.get(1.0, END))
    f.write(ts)
    f.close()


def cut():
    global es
    es = ta.get(SEL_FIRST, SEL_LAST)
    ta.delete(SEL_FIRST, SEL_LAST)


def copy():
    global es
    es = ta.get(SEL_FIRST, SEL_LAST)


def paste():
    global es
    ta.insert(INSERT, es)


def delete():
    ta.delete(SEL_FIRST, SEL_LAST)


def help():
    he = Toplevel(top)
    he.geometry("200x200")
    he.title("정보")
    lb = Label(he, text="메모장 버전 1.0\n 파이썬으로 만든 메모장입니다^^")
    lb.pack()


top = Tk()
top.title("메모장")
top.geometry("400x400")

ta = Text(top)
sb = Scrollbar(ta)
sb.config(command=ta.yview)
top.grid_rowconfigure(0, weight=1)
top.grid_columnconfigure(0, weight=1)
sb.pack(side=RIGHT, fill=Y)
ta.grid(sticky=N + E + S + W)

file = None

mb = Menu(top)
fi = Menu(mb, tearoff=0)
fi.add_command(label="새파일", command=newFile)
fi.add_command(label="열기", command=openFile)
fi.add_command(label="저장", command=saveFile)
fi.add_separator()
fi.add_command(label="종료", command=top.destroy)
mb.add_cascade(label="파일", menu=fi)

e = Menu(mb, tearoff=0)
e.add_command(label="잘라내기", command=cut)
e.add_command(label="복사", command=copy)
e.add_command(label="붙이기", command=paste)
e.add_command(label="삭제", command=delete)
mb.add_cascade(label="편집", menu=e)

h = Menu(mb, tearoff=0)
h.add_command(label="메모장 정보", command=help)
mb.add_cascade(label="도움말", menu=h)

top.config(menu=mb)

top.mainloop()

