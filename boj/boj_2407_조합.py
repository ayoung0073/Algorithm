n, m = map(int, input().split())
idx = 0
mul = 1
div = 1
obj = m

res = 1
while idx != obj:
  mul *= n
  n -= 1
  div *= m
  m -= 1
  idx += 1
  
print(mul // div)
