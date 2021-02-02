# 18406. 럭키스트레이트
n = input()
length = len(n) // 2

comp = 0
for i in range(length):
  comp += int(n[i])

tmp = 0
for i in range(length, len(n)):
  tmp += int(n[i])

if comp == tmp:
  print('LUCKY')
else:
  print('READY')
