# if else 연습
a = 3
if a < 0:
    print('A 는 음수 입니다.')
else:
    print('A 는 양수 입니다.')

# if elif else 염습
a = -25
if a > 0:
    print('A 는 양수 입니다.')
elif a < 0:
    print('A 는 양수 입니다.')
else:
    print('A 는 0 입니다. ')

# if 문 안의 if 문 연습
a = 30
if a > 0:
    if a % 2 == 0:
        print('A 는 짝수 입니다.')
    else:
        print('A 는 홀수 입니다. ')
elif a == 0:
    print('A 는 0 입니다. ')
else:
    print('A 는 음수 입니다. ')

"""
몬스터에게 공격을 당했다. 체력이 100이하면 죽음. 체력이 100 이상이면 체력이 100 감소, 방어력이 있으면 100-방어력 만큼 감소하는
함수를 만들어라. 체력이 0 이하면 이미 사망했다고 메세지를 남김.
"""

# 변수 지정
monster_attack = 100     # 몬스터 공격력
player_health = 250      # 플레이어 체력
player_defence = 30      # 플레이어 방어력


# 몬스터의 공격
def attack(atk, hp):
    global player_defence
    if hp < 0:
        print('플레이어는 이미 사망했다.')
        return hp
    else:
        print(f'플레이어의 체력은 {hp}이다. ')
    print(f'몬스터가 공격 했다. 몬스터가 {atk}만큼 피를 줌')
    hp -= 100 - player_defence
    if hp < 0:
        print('플레이어가 사망했다.')
    else:
        print(f'플레이어의 체력은 {hp}이다.')
    print('------------------------------------------')
    return hp


for i in range(10):
    player_health = attack(monster_attack, player_health)
