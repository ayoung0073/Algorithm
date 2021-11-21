## 9934. 완전 이진 트리
import sys
input = sys.stdin.readline
# 중위 순회

k = int(input())
numbers = list(map(int, input().split()))
tree = [[] for _ in range(k)]

def make_tree(arr, x): 
  mid = len(arr) // 2 # 루트
  tree[x].append(arr[mid])

  if len(arr) == 1:
    return
  
  # (x + 1)행 작업
  make_tree(arr[:mid], x + 1) # 왼쪽
  make_tree(arr[mid + 1:], x + 1) # 오른쪽

make_tree(numbers, 0)
for i in range(k):
  print(*tree[i])
  


