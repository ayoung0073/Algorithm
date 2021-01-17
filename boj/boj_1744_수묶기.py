n = int(input())

nums = []

for _ in range(n):
  nums.append(int(input()))

# 내림차순 후, 묶어보자
num_plus = [i for i in nums if i > 0]
num_plus.sort(reverse=True)

num_minus = [i for i in nums if i <= 0]
num_minus.sort()

count = 0 # 무조건 2이하임
mul = 1
result = 0
for num in num_plus:
# 1을 놓쳤다.. . !
  if num == 1:
    result += num
  else:
    mul *= num
    count += 1

  if count == 2:
    result += mul
    count = 0
    mul = 1

if count == 1:
  result += mul
  count = 0
  mul = 1

for num in num_minus:
  mul *= num
  count += 1
  if count == 2:
    result += mul
    count = 0
    mul = 1
    
if count == 1:
  result += mul

print(result)
