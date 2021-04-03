from tkinter import *
class App:
    def __init__(self, root):
        self.root = root
        self.x = IntVar()
        self.y = IntVar()
        self.frame = Frame(root)
        self.frame.pack()
        self.sport = [("football", 0), ("tennis", 1), ("golf", 2), ("badminton", 3)]
        self.diff = [("easy", 0), ("medium", 1), ("hard", 2)]
        for i, c in self.sport:
            Radiobutton(self.frame, text=i, variable=self.x, value=c, indicatoron=0).pack(anchor="w", fill="both", expand=True)
        for i, c in self.diff:
            Radiobutton(self.frame, text=i, variable=self.y, value=c, indicatoron=0).pack(anchor="w", fill="both", expand=True)
        Button(self.frame, text="Ok", command=self.start).pack(anchor="w", fill="both", expand=True)
    def start(self):
        print("questions: "+self.sport[self.x.get()][0]+", "+"difficulty: "+self.diff[self.y.get()][0])
root = Tk()
App(root)
root.mainloop()