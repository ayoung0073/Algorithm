n = int(input())

ugly = [0] * n # 못생긴 수를 담기 위한 테이블(DP)
ugly[0] = 1

# 2배, 3배, 5배를 위한 인덱스
i2, i3, i5 = 0, 0, 0
# 곱셈값 초기화
two, three, five = 2, 3, 5

# 1부터 n까지의 못생긴 수 찾기
for l in range(1, n):
  ugly[l] = min(two, three, five) # 가장 작은 수
  print(ugly)
  # 인덱스에 다라 곱셈 결과 증가  
  if ugly[l] == two:
    i2 += 1
    two = ugly[i2] * 2
  if ugly[l] == three:
    i3 += 1
    three = ugly[i3] * 3
  if ugly[l] == five:
    i5 += 1
    five = ugly[i5] * 5

print(ugly[n - 1])
