n, m = map(int, input().split())
tree = list(map(int, input().split()))
# tree = list(map(int, sys.stdin.readline().split())) -> 시간단축 O

def cut_tree(tree, height): # 자른 나무의 길이 구하는 함수
  cut_length = 0
  for i in tree:
    if i > height: # 나무의 길이가 절단기 높이보다 클 때만, 자르기 가능
      cut_length += i - height
  return cut_length

# 처음 start: 0, end: max(tree)
def binary_search(tree, start, end): # 이진탐색
  result = 0 
  while start <= end:
    height = (start + end) // 2
    if cut_tree(tree, height) > m:
      start = height + 1 # 오른쪽 탐색(절단기의 높이 +++)
      result = height # 최대한 덜 잘랐을 때가 정답이므로, result에 저장해논다
    elif cut_tree(tree, height) < m:
      end = height - 1 # 왼쪽 탐색(절단기의 높이 ---)
    else:
      return height
  return result
print(binary_search(tree, 0, max(tree)))
