import numpy as np
import pandas as pd


# 시리즈
s = pd.Series([0, 0.25, 0.5, 0.75, 1.0])
print(s)

print(s.values)
print(s.index)
print(s[1])
print(s[1:4])
s = pd.Series([0, 0.25, 0.5, 0.75, 1.0], index=['a', 'b', 'c', 'd', 'e'])
print(s)
print(s.index)
print(s['c'])
print('b' in s)
s = pd.Series([0, 0.25, 0.5, 0.75, 1.0], index=[2, 4, 6, 8, 10])
print(s)
print(s.unique())
print(s.value_counts())
print(s.isin([0.25, 0.75]))
pop_tuple = {'서울특별시': 9728846,
             '부산광역시': 3404423,
             '인천광역시': 2427954,
             '대구광역시': 1235213}
population = pd.Series(pop_tuple)
print(population['서울특별시'])

# 데이터 프레임
d= pd.DataFrame([{'A':2, 'B':4, 'D':3}, {'A': 4, 'B':5, 'C':7}])
print(d)
print(pd.DataFrame(np.random.rand(5,5),
              columns=['A', 'B', 'C', 'D', 'E'],
              index=[1, 2, 3, 4, 5]))

male_tuple = {'서울특별시': 4732275,
             '부산광역시': 1668618,
             '인천광역시': 1476813,
             '대구광역시': 1198815}
male = pd.Series(male_tuple)

female_tuple = {'서울특별시': 4988571,
             '부산광역시': 1735885,
             '인천광역시': 1470404,
             '대구광역시': 1229139}
female = pd.Series(male_tuple)

korea_df = pd.DataFrame({'인구수': population,
                         '남자인구수': male,
                         '여자인구수': female})
print(korea_df)
print(korea_df.index)
print(korea_df['여자인구수'])


# 인덱스 객체
idx = pd.Index([2,4,6,8,10])
print(idx)
print(idx.dtype)
print(idx.ndim)
print(idx.shape)
print(idx.size)
idx1 = pd.Index([1,2, 4, 6, 8])
idx2 = pd.Index([2, 4, 5, 6, 7])
print(idx1.append(idx2))
print(idx1.difference(idx2))
print(idx1.intersection(idx2))
print(idx1.union(idx2))
print(idx1.delete(2))
print(idx1.drop(2))
print(idx1)


# 인덱싱
s = pd.Series([0, 0.25, 0.5, 0.75, 1.0], index=['a', 'b', 'c', 'd', 'e'])
print(s.keys())
print(list(s.items()))
print(s.items())

