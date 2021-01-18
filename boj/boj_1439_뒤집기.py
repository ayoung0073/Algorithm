## 뒤집기
# 다솜이가 할 수 있는 행동은 S에서 연속된 하나 이상의 숫자를 잡고 모두 뒤집는 것이다. 뒤집는 것은 1을 0으로, 0을 1로 바꾸는 것을 의미한다.

data = list(map(int, input()))

cont = []
before = data[0]
num = 1
for i in range(1, len(data)):
  if before != data[i]: # 불연속한 값일 경우,
    cont.append(before) # 값
    before = data[i] # 불연속값을 before에 대입
cont.append(before)

zero = 0
one = 0
for i in cont:
  if i == 0:
    zero += 1
  else:
    one += 1
print(min(zero, one))
