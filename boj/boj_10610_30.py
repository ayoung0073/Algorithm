N = input()
N = sorted(N, reverse=True)

M = list(map(int, N))

check = False
tmp = 0
if 0 not in M: # 10의 배수 체크
  print(-1)
else:
  for num in M:
    tmp += int(num)
  if tmp % 3 == 0: # 각 자리 수 더한 값이 3의 배수인지 체크
    print(''.join(N))
    check = True
  if check == False:
    print(-1)
