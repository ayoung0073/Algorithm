## 1758. 알바생 강호
n = int(input())

tips = []
for _ in range(n):
  tips.append(int(input()))

# 내림차순 정렬
tips = sorted(tips, reverse=True)
result = 0
for i in range(len(tips)):
  rank = i + 1
  tip = tips[i] - (rank - 1)
  if tip > 0:
    result += tip

print(result)
