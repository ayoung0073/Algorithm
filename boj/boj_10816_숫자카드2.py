## 10816. 숫자 카드2

#1 : 순서대로 카드 세기
import sys
input = sys.stdin.readline

n = int(input())
cards = sorted(list(map(int, input().split())))

m = int(input())
sols = list(map(int, input().split()))

dict_sols = {}

idx = 0
for sol in sorted(sols):
  cnt = 0
  if sol not in dict_sols: # 이 조건 없으면 틀림
    while idx < n:
      if cards[idx] == sol:
        cnt += 1
        idx += 1
      elif cards[idx] < sol:
        idx += 1
      else:
        break
    dict_sols[sol] = cnt
  
print(' '.join(str(dict_sols[i]) for i in sols))

#2 : 해시 알고리즘
import sys
input = sys.stdin.readline

n = int(input())
cards = list(map(int, input().split()))

m = int(input())
sols = list(map(int, input().split()))

hashmap = {}

for card in cards:
  if card in hashmap:
    hashmap[card] += 1
  else:
    hashmap[card] = 1

print(' '.join(str(hashmap[i]) if i in hashmap else '0' for i in sols))
