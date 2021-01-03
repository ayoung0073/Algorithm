# 큰 수의 법칙 - 2

# 반복되는 수열에 대해 파악하자

# 배열의 크기 N, 숫자가 더해지는 횟수 M, 최대 연속 개수 K
n, m, k = map(int, input().split())
#print(n, m, k)

# N개의 수를 공백으로 구분하여 입력받기
data = list(map(int, input().split()))
# print(data)

data.sort() # 일단 오름차순으로 정렬
first = data[n - 1]
second = data[n - 2]

# 가장 큰 수(first) 가 나오는 개수 구하기
# 총 더해지는 횟수에 k + 1(1은 반복되는 수열에서 두번째로 큰 수의 개수를 뜻함)
# ex) 5 5 5 3이면 3의 개수.
count = int(m / (k + 1)) * k
# 나누어 떨어지지 않을 경우
count += m % (k + 1)

sum = 0
sum += count * first # 결과 중 가장 큰수의 합
sum += (m - count) * second # 결과 중 두번째로 큰 수의 합

print(sum)
