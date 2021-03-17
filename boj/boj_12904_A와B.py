## 12904. A와 B
import sys
input = sys.stdin.readline

s = list(input().rstrip())
t = list(input().rstrip())

while len(s) != len(t):
  if t[-1] == 'A': 
    t.pop()
  else: # B인 경우
    t.pop()
    t = t[::-1]

if s == t:
  print(1)
else:
  print(0)
