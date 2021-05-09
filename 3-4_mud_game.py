import random
import time

map1 = ([1, 1, 1, 1, 1, 1, 3, 1, 1, 1, 1, 3, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 3, 0, 0, 0],
        [0, 0, 3, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
        [0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0],
        [0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0],
        [0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 3, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 3, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 3, 1, 1, 1, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 3, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 3, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 4, 2],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        )


class Player:
    def __init__(self):
        self.hp = 15
        self.deff = 2
        self.atk = 5
        self.y = 19
        self.x = 17
        self.kill = 0

    def update(self, move):
        if move == 1:
            self.x -= 1
        elif move == 2:
            self.x += 1
        elif move == 3:
            self.y -= 1
        elif move == 4:
            self.y += 1
        elif move == 5:
            if self.hp < 16:
                self.hp += 1
                print(f'체력 {self.hp}')
            else:
                print('더이상 체력이 오르지 않는다.')

    def attack(self, mob):
        while mob.hp > 0:
            print(f'몬스터에게 {self.atk}만큼 피해를 주었다.')
            mob.hp -= self.atk - mob.deff
            print(f'몬스터의 남은 체력은{mob.hp}')

            if mob.hp > 0:
                print(f'몬스터가 반격했다.{mob.atk}.')
                self.hp -= mob.atk - self.deff
            print(f' 너의 남은 체력은 {self.hp}')
            if self.hp < 0:
                print('넌 죽었다.')
                return 0
            time.sleep(2)
        print('몬스터를 죽였다.')
        self.kill += 1
        if self.atk < 9 and self.kill / 3 > self.atk - 5:
            self.atk += 1
            print(f'공격력이 1 증가 했다.공격력{self.atk}')
        else:
            print(f'공격력이 오르지 않았다.공격력{self.atk}')
        del monsters[monsters.index(mob)]
        monsters.append(Monster())
        return 1


class Monster:
    def __init__(self):
        self.hp = random.randint(5, 15)
        self.deff = random.randint(1, 3)
        self.atk = random.randint(4, 7)
        self.y = random.randint(0, 19)
        self.x = random.randint(0, 19)

    def update(self, move):
        if move == 1:
            self.x -= 1
        elif move == 2:
            self.x += 1
        elif move == 3:
            self.y -= 1
        elif move == 4:
            self.y += 1


class Doorman(Monster):
    def __init__(self):
        super().__init__()
        self.hp = 100
        self.deff = 4
        self.atk = random.randint(8, 9)
        self.x = 18
        self.y = 19

    def update(self, _go):
        pass


def next_turn():
    print('다음 턴')
    if map1[player.y][player.x - 1]:
        print('뒤로 갈 수 있다.[1]')
    if map1[player.y][player.x + 1]:
        print('앞으로 갈 수 있다.[2]')
    if map1[player.y - 1][player.x]:
        print('위로 갈 수 있다.[3]')
    if map1[player.y + 1][player.x]:
        print('아래로 갈 수 있다.[4]')
    print('휴식하여 체력을 회복한다.[5]')


player = Player()
monsters = []
for i in range(100):
    monsters.append(Monster())
monsters.append(Doorman())

print('''
눈을 뜨고 깨어 보니 당신은 던젼에 갖혀 있다. 던전을 탈출하여 집에 가야 한다.
주변에는 몬스터가 널려 있다. (100마리)
당신의 앞에서는 나아 갈 수 있는 길이 동서남북으로
되어 있는데, 길을 벗어나면 낭떠러지로 죽게된다.
몬스터를 죽이면 공격력이 오른다.
던전에는 보물상자가 있다. 보물상자를 획득하면 방어력이 오른다.
보물상자는 총 4개이다. 
전전의 크기는 20 X 20 이다. 시작은 0,0 이고 탈출지점은 20,20 이다. 
탈출 지점 앞에는 문지기가 문을 지키고 있다. 강력하니 준비를 하고 싸워야 
탈출 할 수 있다. (보물을 많이 모아야 문지기를 이길 수 있다. )
''')
playing = 1
while playing:
    go = 0

    if map1[player.y][player.x] == 0:
        print('게임이 끝났다.')
        playing = 0
        exit()
    if map1[player.y][player.x] == 2:
        print('던젼을 탈출했다.!!!!')
        exit()
    if map1[player.y][player.x] == 3:
        print('보물 상자를 발견했다. 방어력이 1 오른다.', )
        player.deff += 1

    if map1[player.y][player.x] == 4:
        print('문지기를 만났다. ')

    for monster in monsters:
        if player.x == monster.x and player.y == monster.y:
            print('몬스터를 만났다.')
            go = input('싸울것인가?[1] 도망갈 것인가?[2]')
            go = int(go)
            if go == 1:
                print('플레이어가 공격했다.')
                playing = player.attack(monster)
                if not playing:
                    exit()
            if go == 2:
                player.hp -= 3
                if player.hp < 0:
                    print('넌 죽었다.')
                    exit()

    print('-------------------------------------------')
    next_turn()
    go = ''
    while not go.isdigit():
        go = input('어디로 갈 것인가')

    player.update(int(go))
    for monster in monsters:
        monster.update(random.randint(1, 4))
        if monster.x < 0:
            monster.x = 0
        if monster.x > 20:
            monster.x = 20
        if monster.y < 0:
            monster.y = 0
        if monster.y > 20:
            monster.y = 20
    if player.hp < 10:
        player.hp += 1
        print(f'한턴이 지나서 체력이 1 증가 한다.체력이 {player.hp}가 되었다.')

    print('플레이어', player.x, player.y)
