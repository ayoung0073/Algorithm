## 재귀함수로 구현한 이진탐색
def binary_search_recur(array, target, start, end):
  if start > end: # 시작점이 끝점보다 크면 찾으려는 데이터 없는 것
    return None
  mid = (start + end) // 2 
  # 중간점 찾기
  # mid = int((start + end) / 2) 와 같음

  # 찾으려는 데이터가 중간점의 데이터이면, 찾음 -> 중간점의 인덱스 반환  
  if array[mid] == target:
    return mid 
  elif array[mid] > target:
    return binary_search_recur(array, target, start, mid - 1)
  else:
    return binary_search_recur(array, target, mid + 1, end)

# 원소의 개수 n, 찾으려는 데이터 target
n, target = map(int, input().split())
# 전체 원소 입력 받기
array = list(map(int, input().split()))

# 이진 탐색 수행 결과 출력
result = binary_search_recur(array, target, 0, n - 1)
if result == None:
  print("원소 존재 X")
else:
  print(result + 1)
  

## 반복문으로 구현한 이진탐색
def binary_search_iterable(array, target, start, end):
  while start <= end:
    mid = (start + end) // 2
    if array[mid] == target:
      return mid
    elif array[mid] > target:
      end = mid - 1
    else:
      start = mid + 1
  return None

n, target = map(int, input().split())
array = list(map(int, input().split()))

result = binary_search_iterable(array, target, 0, n - 1)
if result == None:
  print("원소 존재 X")
else:
  print(result + 1)
  
