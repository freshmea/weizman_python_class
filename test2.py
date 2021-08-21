import random, time

import keyboard


class Luck:
    def __init__(self):
        self.luck_list = [['참 운이 좋은 ', '나쁠수도 있고 좋을수도 있는', '좋지 않은', '그냥 그런', '조심해야 할', '아주 나쁜'],
                          ['다만 ', '그러나 ', '항상 ', '하지만 ', '그리고 '],
                          [' 투자를 신경써야', '아주 나쁜일을 대비해야', '하루 종일 기분을 마음껏 뽐내셔야', '자신의 신념을 버리지 말아야', '제대로 긴장해야'],
                          ['욕심을 버려야 하는', '재물운이 높은', '사랑운이 치솟는', '생명운이 올라가는', '운명이 닥치는', '지능운이 탁월히 높게 올라가는']]
        self.chinese_zodiac_sign_list = ['쥐', '소', '범', '토끼', '용', '뱀', '말', '양', '원숭이', '닭', '개', '돼지']
        self.chinese_zodiac_sign = None
        self.chinese_zodiac_sign_num = [random.randint(1, 4), random.randint(1, 4), random.randint(1, 4),
                                        random.randint(1, 4),
                                        random.randint(1, 4), random.randint(1, 4), random.randint(1, 4),
                                        random.randint(1, 4),
                                        random.randint(1, 4), random.randint(1, 4), random.randint(1, 4),
                                        random.randint(1, 4),
                                        random.randint(1, 4)]
        self.luck_string = str()
        self.chinese_zodiac_sign_minus = 0
        self.y = ['1950년 이하:', '1950 ~ 1980:', '1980 ~ 1990:', '1990 ~ 2000:', '그 이상:']


    def radnom_luck(self):
        for i in range(5):
            self.chinese_zodiac_sign_minus = self.chinese_zodiac_sign_num[self.chinese_zodiac_sign_list.index
            (self.chinese_zodiac_sign)]
            print('\n')
            self.luck_string = self.luck_list[0][random.randint(0, 6 - self.chinese_zodiac_sign_minus)] + '날 입니다.' + \
                               self.luck_list[1][random.randint(0, 5 - self.chinese_zodiac_sign_minus)] \
                               + \
                               self.luck_list[2][random.randint(0, 5 - self.chinese_zodiac_sign_minus)] + '합니다. ' + \
                               self.luck_list[3][random.randint(0, 6 - self.chinese_zodiac_sign_minus)] \
                               + \
                               '날 이기도 합니다. (다른 출생년도의 운세를 보시려면 z키를 눌러주세요)'
            print(self.y[i] + self.luck_string)
            while True:
                if keyboard.read_key() == 'z':
                    break

    def chinese_zodiac_sign_test(self):
        self.chinese_zodiac_sign = input('띠 입력(순서대로 쥐, 소, 범, 토끼, 용, 뱀, 말, 양, 원숭이, 닭, 개, 돼지)')


l = Luck()


class Game:
    def __init__(self):
        self.text = ['version: 2.0', 'By ziwootv', 'Youtube YOOZIWOOTV', 'NAVER ZIWOOS', 'SCRATCH jiwootv', '''오늘의 운세 
        나올수 있는 운세 경우 900종류!!!
        엄청난 운세프로그램!''', '다만 운세는 재미로 보는 것이니, 자신에게 맞지 않는 결과가 나와도 뭐라 하지 마세요.',
                     '운세가 맞을 수도 있지만, 또 그렇다고 100% 맞아떨어지는 것은 아닌게 운세니까요.']
        self.load = 0

    def start(self):
        Luck.chinese_zodiac_sign_test(l)
        Luck.radnom_luck(l)
        time.sleep(1)
        print('오늘의 운세 잘 아셨죠? 내일 다시 시도해 보세요!')
        time.sleep(2)
        print('오늘의 운세를 다 읽으셨다면 X키를 눌러 프로그램을 종료하거나, 종료 버튼(×)를 눌러 종료해 주세요.')
        import keyboard
        if keyboard.read_key() == 'X':
            print('3초후 자동종료합니다.')
            for i in range(3):
                print(4 - i)
                time.sleep(1)
            time.sleep(2)
            print('종료합니다.')

    def textprint(self, dlay):
        for num in range(len(self.text)):
            print(self.text[num])
            time.sleep(dlay)

    def print(self):
        for i in range(100):
            print(f'loading...({i + 1}% 완료)')
            self.load = i
            if random.randint(1, 2) == 1:
                time.sleep(0.2)
            else:
                time.sleep(0)
        self.textprint(0.5)


g = Game()
Game.print(g)
Game.start(g)