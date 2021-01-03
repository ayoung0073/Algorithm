# 큰 수의 법칙 - 1

# 배열의 크기 N, 숫자가 더해지는 횟수 M, 최대 연속 개수 K
n, m, k = map(int, input().split())
#print(n, m, k)

# N개의 수를 공백으로 구분하여 입력받기
data = list(map(int, input().split()))
# print(data)

data.sort() # 일단 오름차순으로 정렬
first = data[n - 1]
second = data[n - 2]

sum = 0

while True:
    for i in range(k): # k번 연속해서 더함
        if m == 0: # 숫자 더해지는 횟수가 0이면 break
            break
        sum += first
        m -= 1 # 횟수 하나씩 빼기
    if m == 0:
        break
    sum += second # K번 채워졌을 때는 두번째로 큰 숫자 더하고 다시 while문
    m -= 1

print(sum)
            
