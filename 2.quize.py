import time

"""이 프로그램은 아주 간단한 퀴즈를 만드는 프로그램입니다."""
score = 0
q1=['13+24*2 는 무엇일까요?', '파이 는 무엇일까요?', '파이썬에서 콘솔에 문자를 출력하는 명령어는 무엇일까요?',
    '다음중 물질의 상태가 아닌 것은 무엇 인가요?']

q2=[3, 2, 1, 3]

q3=[[0, 10, 61, 71], [4.23, 3.14, 5.13, 3.15], ['print', 'input', 'get', 'if else'], ['기체', '고체', '물체', '액체']]

def yesorno(a=0):
    global score
    a1=int(input())
    if a1==a:
        print('정답입니다!!!!')
        score = score + 1
    else:
        print('오답입니다!!!!')
    time.sleep(1)
    return

print('아주 쉬운 퀴즈 지금 부터 시작합나다!!! 문제는',len(q1),'문제 입니다.')


for a1, a2 in enumerate(q1):
    print(a1+1, '. 번 문제',a2)
    for b1, b2 in enumerate(q3[a1]):
        print('  ', b1+1, ')', b2)
    yesorno(q2[a1])



"""퀴즈가 끝나고 멘트와 점수를 출력합니다."""
print('퀴즈가 끝났습니다. 당신은 총', score,'개의 문제를 맞혔 습니다.')
print('이 프로그램을 실행해 주셔서 감사합니다. ')
print('produced by Choi Sugil')

