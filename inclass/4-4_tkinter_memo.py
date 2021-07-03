# import tkinter as tk
# from tkinter.filedialog import *
#
# def savef():
#     f = asksaveasfile(mode="w", defaultextension=".txt")
#     if f is None:
#         return
#     ts = str(tx.get(1.0, END))
#     f.write(ts)
#     f.close()
#
# def openf():
#     file = askopenfilename(title="파일 선택", filetypes=(("텍스트 파일", "*.txt"), ("모든 파일", "*.*")))
#     root.title(os.path.basename(file) + " - 메모장")
#     tx.delete(1.0, END)
#     f = open(file, "r")
#     tx.insert(1.0, f.read())
#     f.close()
#
# root = tk.Tk()
#
# root.title('메모장')
# root.geometry('640x480')
#
# mb=tk.Menu(root)
# fm=tk.Menu(mb, tearoff=0)
# mb.add_cascade(label="파일", menu=fm)
# fm.add_command(label='저장', command=savef)
# fm.add_command(label='불러오기', command=openf)
# root.config(menu=mb)
#
# tx=tk.Text()
# tx.pack()
#
# root.mainloop()


# 파이게임 실습
import pygame
import sys
import random

pygame.init()
pygame.display.set_caption('비오는 게임')

Screen_x=640*2
Screen_y=480*2

screen=pygame.display.set_mode((Screen_x, Screen_y))

clock = pygame.time.Clock()

playing = True

class Rain():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = random.randint(5, 18)
        self.bold = random.randint(1, 4)

    def move(self):
        self.y += self.speed

    def off_screen(self):
        return self.y > Screen_y+20

    def draw(self):
        pygame.draw.line(screen, (0,0,0), (self.x, self.y), (self.x, self.y+5), self.bold)

rains=[]
for i in range(100):
    rains.append(Rain(random.randint(10, 630), 10))

while playing:

    """종료시 프로그램 종료시키는 코드"""
    for event in pygame.event.get():
        pass
        if event.type == pygame.QUIT:
            sys.exit()

    rains.append(Rain(random.randint(10, 630), 10))
    clock.tick(60)
    screen.fill((255, 255, 255))
    """빗방울 만들기"""
    for rain in rains:
        rain.move()
        rain.draw()
        if rain.off_screen():
            rains.remove(rain)
            del rain

    pygame.display.update()

