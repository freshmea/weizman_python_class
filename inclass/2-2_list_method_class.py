def 객체이름불러오기(xx):
    return [objname for objname, oid in globals().items() if id(oid) == id(xx)][0]


class 쿠키틀(object):
    쿠키틀사용횟수=0 #클래스 변수

    def __init__(self):
        self.구웠나=0 #객체변수
        쿠키틀.쿠키틀사용횟수+=1


    def 쿠키먹기(self):
        self.name=객체이름불러오기(self)
        if self.구웠나 == 1:
            print(f'{self.name}를 먹었다. 우왕 맛있다. 냠냠')
        else :
            print(f'{self.name}를 먹었다. 쿠키가 안 익었어 퇘퇘!')

    def 쿠키굽기(self):
        self.구웠나=1

    @staticmethod
    def 몇개사용():
        print(f'쿠키툴을 {쿠키틀.쿠키틀사용횟수}개 사용 했습니다.')






빨간쿠키=쿠키틀()
노란쿠키=쿠키틀()

빨간쿠키.쿠키먹기()

노란쿠키.쿠키굽기()
노란쿠키.쿠키먹기()

쿠키틀.몇개사용()


"""리스트에 대해서 연습해 봅니다."""