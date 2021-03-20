"""이 파일은 퀴즈 프로그램입니다."""

a1=0
score=0

def yesorno(a2=0):
    global score
    a1 = input()
    if a1 == a2:
        print('정답입니다.')
        score = score + 1
    else:
        print('오답입니다.')
    return


print('이제부터 퀴즈를 풀겠습니다.')



"""첫문제 코드"""
print('''
1번 문제 다음을 계산하시오. 12+12+40
  1) 54
  2) 64
  3) 74
  4) 84
''')
yesorno(2)



"""두번째문제 코드"""
print('''
2번 문제 다음을 계산하시오. 12+12+42
  1) 55
  2) 66
  3) 77
  4) 88
''')
a1=input()
if a1=='2':
    print('정답입니다.')
    score=score+1
else:
    print('오답입니다.')


"""세번째문제 코드"""
print('''
3번 문제 오빠의 몸무게는
  1) 50
  2) 60
  3) 70
  4) 80
''')
a1=input()
if a1=='4':
    print('정답입니다.')
    score=score+1
else:
    print('오답입니다.')


"""네번째문제 코드"""
print('''
4번 문제 오빠의 고향은?
  1) 성남
  2) 이천
  3) 대전
  4) 계룡
''')
a1=input()
if a1=='1':
    print('정답입니다.')
    score=score+1
else:
    print('오답입니다.')


"""마무리 멘트"""
print('당신의 점수는',score,'점 입니다.')
print('이 프로그램을 사용해 주셔서 감사합니다.')
print('produced by Choi')