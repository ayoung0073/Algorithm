num = [1, 2, 3, 4]
name = ['ayong', 'marie', 'maum', 'maong']

list1 = list(zip(num, name)) # 아이템이 튜플타입인 리스트
dict1 = dict(list1) # 리스트를 딕셔너리 형태로

print(list1)
print(dict1)

'''
[(1, 'ayong'), (2, 'marie'), (3, 'maum'), (4, 'maong')]
{1: 'ayong', 2: 'marie', 3: 'maum', 4: 'maong'}
'''

for n, m in zip(num, name):
  print(n, m)

'''
1 ayong
2 marie
3 maum
4 maong
'''

### 여기는 그냥 테스트
print(set(list1))
print(set(dict1))

'''
{(1, 'ayong'), (3, 'maum'), (4, 'maong'), (2, 'marie')}
{1, 2, 3, 4}
'''
