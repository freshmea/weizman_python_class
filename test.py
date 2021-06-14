import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()
        self.package()

    def create_widgets(self):
        self.hi_there = tk.Button(self, text="Hello World\n(click me)", command=self.say_hi)
        self.quit = tk.Button(self, text="QUIT", fg="red", command=self.master.destroy)

    def package(self):
        self.hi_there.pack(side="top")
        self.quit.pack(side="bottom")

    def say_hi(self):
        print("hi there, everyone!")

root = tk.Tk()
app = Application(master=root)
app.mainloop()