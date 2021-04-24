
empty_dict = {}
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}

person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
    }


print(len(dct)) # 4
print(len(person)) # 7

print(person['first_name']) # Asabeneh
print(person['country'])    # Finland
print(person['skills'])     # ['JavaScript', 'React', 'Node', 'MongoDB', 'Python']
print(person['skills'][0])  # JavaScript
print(person['address']['street']) # Space street
# print(person['city'])       # Error

print(person.get('first_name')) # Asabeneh
print(person.get('country'))    # Finland
print(person.get('skills')) #['HTML','CSS','JavaScript', 'React', 'Node', 'MongoDB', 'Python']
print(person.get('city'))   # None

person['job_title'] = 'Instructor'
person['skills'].append('HTML')
print(person)

person['first_name'] = 'Eyob'
person['age'] = 18
print(person)


fruits = {'banana', 'orange', 'mango', 'lemon'}
print('mango' in fruits)

#추가 하기
fruits.add('lime')

vegetables = ('tomato', 'potato', 'cabbage','onion', 'carrot')
fruits.update(vegetables)

print(fruits)

#제거하기 랜덤
fruits.pop()
#제거하기 지정
fruits.remove('tomato')
print(fruits)

python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}

# 합집합
union_py_dr = python | dragon
print(union_py_dr)

# 교집합
it_py_dr = python & dragon
print(it_py_dr)

# 차집합
di_py_dr = python - dragon
di_dr_py = dragon - python
print(di_py_dr, di_dr_py)


