import time

"""이 프로그램은 아주 간단한 퀴즈를 만드는 프로그램입니다."""
a1=0
score=0

print('아주 쉬운 퀴즈 지금 부터 시작합나다!!! 문제는3문제 입니다.')


"""이것은 첫 번째 문제에 관련된 코드입니다."""
print('''
1.번 문제 13+24*2 는 무엇일까요?
  1) 0
  2) 100
  3) 61
  4) 71
''')
a1=int(input())

if a1==3:
    print('정답입니다!!!!')
    score=score+1
else:
    print('오답입니다!!!!')
time.sleep(1)


"""이것은 두 번째 문제에 관련된 코드입니다."""
print('''
2.번 문제 파이 는 무엇일까요?
  1) 4.23
  2) 3.14
  3) 5.13
  4) 3.15
''')
a1=int(input())

if a1==2:
    print('정답입니다!!!!')
    score=score+1
else:
    print('오답입니다!!!!')
time.sleep(1)



"""퀴즈가 끝나고 멘트와 점수를 출력합니다."""
print('퀴즈가 끝났습니다. 당신의 점수는', score,'입니다.')
print('이 프로그램을 실행해 주셔서 감사합니다. ')
print('produced by choi su gil')

