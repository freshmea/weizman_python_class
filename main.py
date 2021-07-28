# 계산기!
import keyboard
import time


class Calculation:
    def __init__(self):  # 변수 설정
        # 변수를 self 지정.
        self.answer1 = 0  # 첫 번째 수
        self.answer2 = 0  # 두 번째 수
        self.result = 0  # 결과
        self.attribution = 0  # 곱셈인가 나눗셈인가 덧셈인가 뺄셈인가
        self.say1 = ['계산기!', '버전 1.0\nby . 파이썬', '안녕하세요!\nQ키는 더하기, W키는 빼기, E키는 곱하기, R키는 나누기 입니다!\n그럼 잘 쓰세요!']  # 착한 설명 ㅎ
        self.say2 = ['+', '-', '×', '÷']  # 기호
        self.Y_or_N = 0  # (말 그대로 YES OR NO)
        self.num = 0  # (숫자)

    def key(self):
        while True:  # (아래쪽은 노가다의 산물입니다..)
            if keyboard.read_key() == "q":  # 여기만 설명 넣겠습니다.
                self.attribution = 1  # <=  사칙연산 어떤건지 나타내는거 (1: + 2: - 3: × 4: ÷)
                print(self.say2[self.attribution])  # 아까 보았던 것(위에 say2 리스트)
                break  # ???: 멈춰!
            if keyboard.read_key() == "w":
                self.attribution = 2
                print(self.say2[self.attribution])
                break
            if keyboard.read_key() == "e":
                self.attribution = 3
                print(self.say2[self.attribution])
                break
            if keyboard.read_key() == "r":
                self.attribution = 4
                print(self.say2[self.attribution])
                break

    def input(self):
        self.answer1 = int(input('첫 번째로 계산하실 숫자는 무엇인가요?'))
        self.answer2 = int(input('두 번째로 계산하실 숫자는 무엇인가요?'))
        calc.key()

        if self.attribution == 1:
            self.result = self.answer1 + self.answer2
        if self.attribution == 2:
            self.result = self.answer1 - self.answer2
        if self.attribution == 3:
            self.result = self.answer1 * self.answer2
        if self.attribution == 4:
            self.result = self.answer1 / self.answer2

    def result_print(self):
        print('결과는' + str(self.result))
        time.sleep(1)
        self.Y_or_N = input('다시 계산합니까? (다시 계산: Y)')
        if self.Y_or_N == 'Y' or self.Y_or_N == 'y':
            calc.run()

    def run(self):
        for i in range(0, 2):
            self.num += 1
            calc.say(self.num, 2)
        calc.input()
        calc.result_print()

    def say(self, number, delay):
        print(self.say1[number])
        time.sleep(delay)


calc = Calculation()
calc.run()