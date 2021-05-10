a = input('숫자나 소수, 문자열을 입력하세요:')

if a.isalpha():
    print('입력한 값은 문자열')
elif '.' in a:
    a = a.replace('.', '0', 1)
    if a.isdigit():
        print('입력한 값은 소수')
    else:
        print('문자열도 소수도 정수도 아님')
else:
    if a.isdigit():
        print('입력한 값은 정수')
    else:
        print('문자열도 소수도 정수도 아님')
