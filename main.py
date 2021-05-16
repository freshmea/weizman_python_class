setType1 = {1, 2, 3, 4}
setType2 = {3, 4, 5, 6, 7, 8}

unionset = setType1.union(setType2) #합집합
interset = setType1.intersection(setType2) #교집합
difference1 = setType1.difference(setType2) #차집합
difference2 = setType2.difference(setType1)
print(unionset ,'\n' ,interset ,'\n' ,
      difference1 ,'\n' ,difference2)

print(setType1 - setType2) #차집합
print(setType1 & setType2) #교집합
print(setType1 | setType2) #합집합

