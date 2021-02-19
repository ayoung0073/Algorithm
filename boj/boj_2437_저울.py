import sys
input = sys.stdin.readline

n = int(input())
weights = sorted(list(map(int, input().split())))
comp = 1
for weight in weights:
  if comp >= weight:
    comp += weight
  # 해당 무게가 comp보다 크면 더이상 만들 수 없는 금액
  else:
    break

print(comp)
