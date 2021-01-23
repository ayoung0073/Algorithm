## 10814. 나이순 정렬
import sys
input = sys.stdin.readline
n = int(input().strip())
infos = []

for _ in range(n):
  age, name = input().split()
  infos.append((int(age), name))

infos.sort(key = lambda x : x[0]) # 나이순 오름차순

for info in infos:
  print(info[0], info[1]) 
