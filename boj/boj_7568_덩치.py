''' 
입력 예시

5
55 185
58 183
88 186
60 175
46 155
'''

## 브루트포스 / 총 4 + 3 + 2 + 1 = 10번의 비교 연산
import sys
input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n):
  x, y = map(int, input().split())
  arr.append((x, y))

order = [0 for _ in range(n)]
for i in range(n - 1):
  for j in range(i + 1, n):
    if arr[i][0] > arr[j][0] and arr[i][1] > arr[j][1]:
      order[j] += 1
    elif arr[i][0] < arr[j][0] and arr[i][1] < arr[j][1]:
      order[i] += 1
  
print(' '.join(str(i + 1) for i in order))


## set 자료형 이용 / 총 6번의 비교 연산
import sys
input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n):
  x, y = map(int, input().split())
  arr.append((x, y))

order = [set() for _ in range(n)]

for i in range(n - 1):
  for j in range(i + 1, n):
    if i in order[j] or j in order[i]:
      continue
    elif arr[i][0] > arr[j][0] and arr[i][1] > arr[j][1]:
      order[j].add(i)
      order[j].update(order[i])
    elif arr[i][0] < arr[j][0] and arr[i][1] < arr[j][1]:
      order[i].add(j)
      order[i].update(order[j]) 

  
print(' '.join(str(len(i) + 1) for i in order))
