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