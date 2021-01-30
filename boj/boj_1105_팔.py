l, r = input().split()

if len(l) < len(r): # 자릿수 작을 때
  print(0)

elif len(l) == len(r):
  result = 0
  for i in range(len(l)):
    if l[i] != r[i]:
      break
    if l[i] == r[i] == '8':
      result += 1
  print(result)
