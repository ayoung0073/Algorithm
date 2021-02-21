import sys 
input = sys.stdin.readline

n, m = map(int, input().split())
words = {}
for _ in range(n):
  word = input().rstrip()
  if len(word) < m:
    continue
  if not word in words:
    words[word] = 1
  else:
    words[word] += 1

t = list(words.items())

t.sort(key=lambda x : (-x[1], -len(x[0]), x[0]))

for i in t:
  print(i[0])
