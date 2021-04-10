"""아래 나오는 문장과 코드를 직접 타이핑으로 작성하세요."""


# 한줄
letter = 'P'
print(letter)  # P
print(len(letter))  # 1
greeting = 'Hello, World!'  #
print(greeting)  # Hello, World!
print(len(greeting))  # 13
sentence = "I hope you are enjoying 30 days of python challenge"
print(sentence)

# 여러줄 작성
multiline_string = '''I am a teacher and enjoy teaching.
I didn't find anything as rewarding as empowering people.
That is why I created 30 days of python.'''
print(multiline_string)
# 여러줄 또다른 방법
multiline_string = """I am a teacher and enjoy teaching.
I didn't find anything as rewarding as empowering people.
That is why I created 30 days of python."""
print(multiline_string)

# 스트링  다루기
first_name = 'Asabeneh'
last_name = 'Yetayeh'
space = ' '
full_name = first_name + space + last_name
print(full_name)  # Asabeneh Yetayeh

# 스트링의 길이 확인
print(len(first_name))  # 8
print(len(last_name))  # 7
print(len(first_name) > len(last_name))  # True
print(len(full_name))  # 15


# 인덱스로 스트링 다루기
language = 'Python'
first_letter = language[0]
print(first_letter)  # P
second_letter = language[1]
print(second_letter)  # y
last_index = len(language) - 1
last_letter = language[last_index]
print(last_letter)  # n

# 인덱스의 -정수 표현
language = 'Python'
last_letter = language[-1]
print(last_letter)  # n
second_last = language[-2]
print(second_last)  # o

# 슬라이싱 예제

language = 'Python'
first_three = language[0:3]
last_three = language[3:6]
print(last_three)  # hon

# 슬라이싱 또다른 예제
last_three = language[-3:]
print(last_three)  # hon
last_three = language[3:]
print(last_three)  # hon

# 슬라이싱을 두칸씩 건너띄는 방법
language = 'Python'
pto = language[0:6:2]  #
print(pto)  # pto

# 이스케이프 문자 사용
print('I hope every one enjoying the python challenge.\nDo you ?')  # line break
print('Days\tTopics\tExercises')
print('Day 1\t3\t5')
print('Day 2\t3\t5')
print('Day 3\t3\t5')
print('Day 4\t3\t5')
print('This is a back slash  symbol (\\)')  # To write a back slash
print('In every programming language it starts with \"Hello, World!\"')

## 스트링 메소드 연습
# capitalize(): 첫글자를 대문자로 변경

challenge = 'thirty days of python'
print(challenge.capitalize())  # 'Thirty days of python'

# count(): 문자열 안에 몇개가 있는지 숫자를 리턴

challenge = 'thirty days of python'
print(challenge.count('y'))  # 3
print(challenge.count('y', 7, 14))  # 1
print(challenge.count('th'))  # 2`

# endswith(): 마지막에 오는 문자를 확인

challenge = 'thirty days of python'
print(challenge.endswith('on'))  # True
print(challenge.endswith('tion'))  # False

# expandtabs(): 탭의 사이즈를 변경

challenge = 'thirty\tdays\tof\tpython'
print(challenge.expandtabs())  # 'thirty  days    of      python'
print(challenge.expandtabs(10))  # 'thirty    days      of        python'

# find(): 글자가 어디 있는인 인덱스를 리턴

challenge = 'thirty days of python'
print(challenge.find('y'))  # 5
print(challenge.find('th'))  # 0

# format()	스트링의 포맺을 지정
first_name = 'Asabeneh'
last_name = 'Yetayeh'
job = 'teacher'
country = 'Finland'
sentence = 'I am {} {}. I am a {}. I live in {}.'.format(first_name, last_name, job, country)
print(sentence)  # I am Asabeneh Yetayeh. I am a teacher. I live in Finland.

radius = 10
pi = 3.14
area = pi  # radius ## 2
result = 'The area of circle with {} is {}'.format(str(radius), str(area))
print(result)  # The area of circle with 10 is 314.0

# isalnum(): 알파벳과숫자로 이루어지는지 확인

challenge = 'ThirtyDaysPython'
print(challenge.isalnum())  # True

challenge = '30DaysPython'
print(challenge.isalnum())  # True

challenge = 'thirty days of python'
print(challenge.isalnum())  # False

challenge = 'thirty days of python 2019'
print(challenge.isalnum())  # False

# isalpha(): 알파벳으로 이루어졌는지 확인

challenge = 'thirty days of python'
print(challenge.isalpha())  # True
num = '123'
print(num.isalpha())  # False

# isdigit(): 숫자로 이루어졌는지 확인

challenge = 'Thirty'
print(challenge.isdigit())  # False
challenge = '30'
print(challenge.isdigit())  # True

# isdecimal():Checks decimal characters

num = '10'
print(num.isdecimal())  # True
num = '10.5'
print(num.isdecimal())  # False

# isidentifier(): 적합한 변수명인지 확인

challenge = '30DaysOfPython'
print(challenge.isidentifier())  # False, because it starts with a number
challenge = 'thirty_days_of_python'
print(challenge.isidentifier())  # True

# islower(): 소문자로만 이루어졌는지 확인

challenge = 'thirty days of python'
print(challenge.islower())  # True
challenge = 'Thirty days of python'
print(challenge.islower())  # False

# isupper(): 대문자로만 이루어졌는지 확인

challenge = 'thirty days of python'
print(challenge.isupper())  # False
challenge = 'THIRTY DAYS OF PYTHON'
print(challenge.isupper())  # True

# isnumeric(): 숫자로만 이루어졌는지 확인

num = '10'
print(num.isnumeric())  # True
print('ten'.isnumeric())  # False

# join(): 리스트를 합쳐줌

web_tech = ['HTML', 'CSS', 'JavaScript', 'React']
result = '#, '.join(web_tech)
print(result)  # 'HTML# CSS# JavaScript# React'

# strip(): Removes both leading and trailing characters

challenge = ' thirty days of python '
print(challenge.strip())  # thirty days of python

# replace(): Replaces substring inside

challenge = 'thirty days of python'
print(challenge.replace('python', 'coding'))  # 'thirty days of coding'

# split(): 단어로 나누어서 리스트를 만듬

challenge = 'thirty days of python'
print(challenge.split())  # ['thirty', 'days', 'of', 'python']

# title(): 모든 단어의 첫 글자를 대문자로 바꿈

challenge = 'thirty days of python'
print(challenge.title())  # Thirty Days Of Python

# swapcase(): 대문자는 소문자로 소문자는 대문자로 바꿈

challenge = 'thirty days of python'
print(challenge.swapcase())  # THIRTY DAYS OF PYTHON
challenge = 'Thirty Days Of Python'
print(challenge.swapcase())  # tHIRTY dAYS oF pYTHON

# startswith(): 첫 문장이 비교문자와 같은지 비교

challenge = 'thirty days of python'
print(challenge.startswith('thirty'))  # True
challenge = '30 days of python'
print(challenge.startswith('thirty'))  # False