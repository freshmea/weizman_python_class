# print('Hello world')    #이것은 우리가 만든 첫 코드입니다.
# # number1=3.141592
# # number2=6.455213
#
#
#
# #두 숫자를 입력 받아서 계산해 주는 코드입니다.
#
#
# number1=int(input('첫번째 숫자:'))
# number2=int(input('두번째 숫자:'))
#
# print('첫번째 숫자는:', number1,'두번째 숫자는:', number2)
# print('두 숫자의 합은 :', number1+number2)
# print('두 숫자의 곱은 :', number1*number2)
# print('두 숫자의 나누기는 :', number1/number2)
#
# #이름을 입력 받아서 정보를 출력하는 코드입니다.
# char=input('이름을 입력하세요:')
# print(char+'은 계룡에 살고 있습니다.')
# print(char+'은 30살 입니다.')
# print(char+'은 선생닙입니다.')
# print(char+'의 취미는 컴퓨터 입니다.')
#
#
#
#
#

from threading import Timer
timeout = 5
t = Timer(timeout, print, ['Sorry, times up'])
t.start()
prompt = "You have %d seconds to choose the correct answer...\n" % timeout
try:
    answer = input(prompt)
except:
    print('df')
print(answer)
t.cancel()

