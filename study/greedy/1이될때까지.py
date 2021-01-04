import time

# 나
n, k = map(int, input().split())
start = time.time()
result = 0
while n != 1:
  if(n % k == 0):
    n //= k
  else:
    n -= 1
  result += 1

  
first = time.time() - start
print(first)
print(result)


# 단순하게 푸는 답안
n, k = map(int, input().split())
start = time.time()
result = 0

# N이 K 이상이라면 K로 계속 계속 나누기
while n >= k:
  while n% k != 0:
    n -=  1
    result += 1
  
  n //= k
  result += 1

while n > 1:
  n -= 1
  result += 1


second = time.time() - start
print(second)
print(result)

#  N이 100억 이상의 큰 수가 되는 경우를 가정했을 때에도 빠르게 동작하려면, N이 K의 배수가 되도록 효율적으로 한 번에 빼는 방식으로 소스코드 작성할 수 있음

## 예시
n, k = map(int, input().split())
start = time.time()
result = 0

while True:
  # N이 K로 나누어떨어지는 수가 될 때까지 1씩 뺌
  target = (n // k) * k
  result += (n - target) # 1씩 빼는 거임
  n = target
  # N이 K보다 작을 때(더이상 나눌 수 없을 때 반복문 종료)
  if n < k:
    break
  # k로 나누기
  result += 1
  n //= k

# 마지막으로 남은 수에 대해 1씩 뺌
result += (n - 1)

third = time.time() - start
print(third)
print(result)

print(min(first, second, third))
print(max(first, second, third))

# 시간 빠름 3 -> 1 -> 2
