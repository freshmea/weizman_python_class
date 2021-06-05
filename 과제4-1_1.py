import tkinter as tk
import tkinter.scrolledtext as tkst
from tkinter import Menu
from tkinter import ttk


def clickOK():
    text = "너의 성별은  " + gender.get()
    text = text + "\n너는  " + str(age.get()) + " 살이다..\n"
    scrt.insert(tk.INSERT, text)
    scrt.see(tk.END)


def clickRadio():
    scrt.insert(tk.INSERT, value3.get())
    scrt.see(tk.END)


def clickExit():
    win.quit()
    win.destroy()
    exit()


if __name__ == '__main__':
    win = tk.Tk()
    win.title("tkinter sample")

    labelGender = ttk.Label(win, text="성별:")
    labelGender.grid(column=0, row=0)

    labelAge = ttk.Label(win, text="나이:")
    labelAge.grid(column=1, row=0)

    gender = tk.StringVar()
    genderCombo = ttk.Combobox(win, width=6, textvariable=gender)
    genderCombo['values'] = ("남자", "여자")
    genderCombo.grid(column=0, row=1)
    genderCombo.current(0)

    age = tk.IntVar()
    ageEntered = ttk.Entry(win, width=3, textvariable=age)
    ageEntered.grid(column=1, row=1)

    action = ttk.Button(win, text="OK", command=clickOK)
    action.grid(column=2, row=1)

    scrt = tkst.ScrolledText(win, width=33, height=3, wrap=tk.WORD)
    scrt.grid(column=0, row=2, columnspan=3)
    scrt.focus_set()

    value1 = tk.IntVar()
    check1 = tk.Checkbutton(win, text="비활성화", variable=value1, state='disabled')
    check1.select()
    check1.grid(column=0, row=3)

    value2 = tk.IntVar()
    check2 = tk.Checkbutton(win, text="체크 안됨", variable=value2)
    check2.grid(column=1, row=3)

    value3 = tk.StringVar()
    rad1 = tk.Radiobutton(win, text="Radio1", variable=value3, value="라디오1버튼 누름.\n",
                          command=clickRadio)
    rad1.select()
    rad1.grid(column=2, row=3)
    rad2 = tk.Radiobutton(win, text="Radio2", variable=value3, value="라디오2버튼 누름.\n",
                          command=clickRadio)
    rad2.grid(column=2, row=4)

    menuBar = Menu(win)
    win.config(menu=menuBar)

    fileMenu = Menu(menuBar, tearoff=0)
    fileMenu.add_command(label="New")
    fileMenu.add_separator()
    fileMenu.add_command(label="Exit", command=clickExit)
    menuBar.add_cascade(label="File", menu=fileMenu)

    win.resizable(0, 0)
    win.mainloop()