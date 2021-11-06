## 2493. 탑

n = int(input())
top_list = list(map(int, input().split()))
stack = []
answer = [0] * n

for i in range(n):
  if not stack:
    answer[i] = 0
  while stack:
    if stack[-1][1] > top_list[i]:
      answer[i] = stack[-1][0] + 1
      break
    else:
      stack.pop() 

  stack.append([i, top_list[i]])
print(" ".join(str(i) for i in answer))
