# set 함수 이용
# l, s = map(int, input().split())
# #listen = []
# #see = []

# listen = set()
# see = set()

# for i in range(l):
#   listen.add(input())
# for j in range(s):
#   see.add(input())
# count = 0
# result = list(listen & see)
# result.sort()

# print(len(result))
# for i in result:
#   print(i)


# 시간 초과 방지 sys 라이브러리 이용!

import sys
l, s = map(int, input().split())
listen = [sys.stdin.readline().rstrip() for i in range(l)]
see = [sys.stdin.readline().rstrip() for i in range(s)]

result = sorted(list(set(listen) & set(see)))
print(len(result))
for i in result:
  print(i)
