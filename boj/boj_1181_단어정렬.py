#### 위상정렬 이용
import sys

input = sys.stdin.readline
n = int(input())
words = [[] for i in range(51)] # 길이 50으로 맞추자
for _ in range(n):
  word = input().strip() # strip() 안 하면 \n 덧붙여짐
  length = len(word)
  words[length].append(word)

for array in words:
  array = set(array)
  array = list(array)
  for i in sorted(array):
    print(i)


#### lambda식 이용
import sys

input = sys.stdin.readline
n = int(input())
words_tuple = []
for _ in range(n):
    word = input().strip()
    words_tuple.append((word, len(word))) # 튜플 이용

words_tuple = list(set(words_tuple)) #중복 삭제

#단어 숫자 정렬 > 단어 알파벳 정렬
words_tuple.sort(key = lambda word: (word[1], word[0]))

for word in words_tuple:
    print(word[0])
