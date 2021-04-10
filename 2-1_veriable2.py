# a='여기는\n와이즈만\n입니다.'
# b='''여기는
# 와이즈만
# 입니다.
# '''
# c='여기는 \t 와이즈만 \t 입니다.\n 여기는 \t 집 \t 입니다.'
# print(type(a))
# print(a)
# print(b)
# print(c)
# score=60
# sen='멋지네요.'
# print('당신의 점수는 %d 입니다.%s'%(score,sen))
# print('당신의 점수는 {} 입니다.{}'.format(score, sen))
# print('당신의 점수는 {1} 입니다.{0}'.format(score, sen))
# print(f'당신의 점수는 {score} 입니다.{sen}')

# string='      this is my python project.ppp'
# print(len(string))
# print(string.find('p'))
# print(string.count('p'))
# print(string)
# print(string.strip())
# string_split= string.split()
# print(string_split)

an=str()
while not (an.isnumeric() and len(an) == 11 and an[0:3]=='010'):
    an=input('전화번호를 입력해 주세요. 숫자만 입력해 주세요. 11자리를 입력해야 합니다.')
an2=an[0:3]+'-'+an[3:7]+'-'+an[7:11]
print(f'당신이 입력한 전화번호는 {an2}입니다.')
