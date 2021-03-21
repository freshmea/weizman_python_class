import tkinter
import time





"""이 프로그램은 아주 간단한 퀴즈를 만드는 프로그램입니다."""
score = 0
check = 0
q1=['13+24*2 는 무엇일까요?', '파이 는 무엇일까요?', '파이썬에서 콘솔에 문자를 출력하는 명령어는 무엇일까요?',
    '다음중 물질의 상태가 아닌 것은 무엇 인가요?', '다음중 색깔이 아닌 것은?']
q2=['', '3', '2', '1', '3', '1']
q3=[['0', '10', '61', '71'], ['4.23', '3.14', '5.13', '3.15'], ['print', 'input', 'get', 'if else'], ['기체', '고체', '물체', '액체'], ['조정', '빨강', '노랑', '검정', '붉그스름']]

"""정답과 오답을 알려주는 함수"""
def yesorno(a='', a1=''):
    global score, check
    if a1==a and not a=='':
        label2.config(text="정답입니다.")
        score = score + 1
    elif a1==a and a=='':
        pass
    else:
        label2.config(text="오답입니다!!!!")
    time.sleep(1)
    return

window=tkinter.Tk()

window.title("최수길-퀴즈프로그램 V 1.0")
window.geometry("640x400+100+100")
window.resizable(False, False)

label1=tkinter.Label(window, text="다음에 나오는 퀴즈를 풀어 주세요.")
label1.config(font=("Courier", 20))
label1.pack()
label2=tkinter.Label(window, text='아주 쉬운 퀴즈 지금 부터 시작합나다!!! 문제는'+str(len(q1))+'문제 입니다.')
label2.config(font=("Courier", 10))
label2.pack()
label3=tkinter.Label(window, text='여기에 문제가 출제 됩니다. 엔터키를 누루면 시작합니다.', anchor='n', fg='red')
label3.config(font=("Courier", 10), )
label3.pack()

def problem(event):
    global check
    if not check==len(q1)+1:
        aa = entry.get()
        if check<len(q1):
            text = str()
            text = text + str(check + 1) + '.번 문제 ' + q1[check]
            for b1, b2 in enumerate(q3[check]):
                text = text + '\n'
                text = text + '  ' + str(b1 + 1) + ')' + str(b2)
            label3.config(text=text)
        yesorno(q2[check], aa)
        check+=1
    else:
        label2.config(text='수고하셨어요')
        label3.config(text='풀어주셔서 감사합니다.')
    entry.delete(0, "end")
    label1.config(text='당신의 점수는'+str(score*10)+'입니다.')
    pass

entry=tkinter.Entry(window)
entry.bind("<Return>", problem)
entry.config(font=("Courier", 20))
entry.pack()


window.mainloop()
