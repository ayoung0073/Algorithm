import sys

input = sys.stdin.readline
n = int(input())
info = []
for _ in range(n):
  name, ko, eng, math = input().split()
  ko = int(ko)
  eng = int(eng)
  math = int(math)
  info.append((name, ko, eng, math))

info.sort(key=lambda x : (-x[1], x[2], -x[3], x[0]))

for i in info:
  print(i[0])
