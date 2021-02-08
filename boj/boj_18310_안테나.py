import sys
input = sys.stdin.readline

n = int(input())
houses = list(map(int, input().split()))
houses.sort() # 오름차순 정렬

if len(houses) % 2 == 0: # 짝수인 경우
  result = houses[len(houses) // 2 - 1]
else:
  result = houses[len(houses) // 2]

print(result)
