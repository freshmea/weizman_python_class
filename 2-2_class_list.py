# def 객체이름불러오기(xx):
#     return [objname for objname, oid in globals().items() if id(oid) == id(xx)][0]
#
#
# class 쿠키틀:
#     def 쿠키굽기(self):
#         print(f'{객체이름불러오기(self)}가 구워졌어요.')
#     pass
#
#
# 빨간_쿠키=쿠키틀()
# 노란_쿠키=쿠키틀()
# 파란_쿠키=쿠키틀()
#
# 빨간_쿠키.쿠키굽기()
# 노란_쿠키.쿠키굽기()
# 파란_쿠키.쿠키굽기()
#
# a = str('a를 넣는다.')
#
# b='a를 넣는다.'
#
# print(a.find('넣'))
# print(type(a), type(b))



"""리스트 연습"""
alist=list(['1번', '2번', 3, 3.14])
blist=['abcd', 'efgh', 123, 456]

print(len(alist))
print(type(blist))
print(blist)

fruits = ['banana', 'orange', 'mango', 'lemon']                     # 과일 리스트
vegetables = ['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot']      # 야채 리스트
animal_products = ['milk', 'meat', 'butter', 'yoghurt']             # 동물 제품 리스트
web_techs = ['HTML', 'CSS', 'JS', 'React','Redux', 'Node', 'MongDB'] # 기술 리스트
countries = ['Finland', 'Estonia', 'Denmark', 'Sweden', 'Norway'] # 나라 리스트

# 각 리스트와 리스트의 길이 출력
print('과일:', fruits)
print('과일 갯수:', len(fruits))
print('야채:', vegetables)
print('야채 갯수:', len(vegetables))
print('동물 식품:',animal_products)
print('동물 식품 갯수:', len(animal_products))
print('인터넷 기술:', web_techs)
print('인터넷 기술 갯수:', len(web_techs))
print('국가:', countries)
print('국가 갯수:', len(countries))

an=input('과일, 야채, 동물, 인터넷기술, 국가 중 하나를 입력하세요: ')
ab=''
for i in fruits:
    if an == i:
        ab='과일'
for i in vegetables:
    if an == i:
        ab='야채'
for i in animal_products:
    if an == i:
        ab='동물제품'
for i in web_techs:
    if an == i:
        ab='웹기술'
for i in countries:
    if an == i:
        ab='나라'

print(an,'는', ab, '입니다.')