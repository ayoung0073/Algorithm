n = int(input())
k = int(input())
start, end = 1, k

while start <= end:
    mid = (start + end) // 2
    
    count = 0
    for i in range(1, n + 1):
      # 이진 탐색으로 어떤 수(mid)보다 작은 자연수의 곱(i * j)이 몇 개(count)인지 알아낸다.
      count += min(mid // i, n)

    if count >= k: # 이진 탐색
        answer = mid
        end = mid - 1
    else:
        start = mid + 1

print(answer)
