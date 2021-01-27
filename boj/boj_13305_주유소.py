n = int(input()) # 도시의 개수

lengths = list(map(int, input().split()))
prices = list(map(int, input().split()))

# 자기 자신보다 price가 작은 도시를 만날 때까지 오른쪽으로 이동해보자
result = 0

price = prices[0]
count = lengths[0]

result += price * count
for i in range(1, n - 1):
  if prices[i] > price:
    result += lengths[i] * price
  else:
    price = prices[i]
    count = lengths[i]
    result += price * count

print(result)
