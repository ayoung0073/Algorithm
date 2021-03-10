import sys
input = sys.stdin.readline

n, k = map(int, input().split())
d = {}
for _ in range(n):
  m, a, b, c = map(int, input().split())
  if (a, b, c) in d:
    d[(a, b, c)].append(m)
  else:
    d[(a, b, c)] = [m]

# print(d.items())
sdict = sorted(d.items(), key = lambda x : (-x[0][0], -x[0][1], -x[0][2]))
idx = 0
for i in range(len(sdict)):
  if k in sdict[i][1]:
    print(idx + 1)
    break
  if len(sdict[i][1]) > 1: # 같은 순위인 나라가 많은 경우, 순위 넘기기
    idx += len(sdict[i][1])
  else:
    idx += 1
