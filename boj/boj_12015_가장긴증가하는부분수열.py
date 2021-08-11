## 가장 긴 증가하는 부분 수열 

import sys
from bisect import bisect_left
input = sys.stdin.readline 

n = int(input())
arr = list(map(int, input().split()))

save = [arr[0]]

for i in arr[1:]:
  if i > save[-1]:
    save.append(i)
  else:
    idx = bisect_left(save, i)
    save[idx] = i

# 현재 값이 마지막 값보다 작은 경우 마지막 값을 대체해야 하는데, 그 앞의 값들보단 커야한다.
# 부분 수열을 구하는 것이 아니라 부분 수열의 길이를 구하는 것이기 때문에 이진 탐색을 통해 앞의 값을 현재 값으로 대체한다.

print(len(save))
