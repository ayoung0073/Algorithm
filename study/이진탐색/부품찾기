n = int(input())
#arr_n = list(map(int, input().split()))
arr_n = set(map(int, input().split())) # 전체 부품은 list 말고 set!!

m = int(input())
arr_m = list(map(int, input().split()))

# 배열 in 이용 --> set 이용하면 더 좋다
def list_in(arr_n, arr_m):
  for i in arr_m:
    if i in arr_n:
      print("yes", end = ' ')
    else:
      print("no", end = ' ')

list_in(arr_n, arr_m)

print()

n = int(input())
arr_n = list(map(int, input().split()))

m = int(input())
arr_m = list(map(int, input().split()))

# 이진탐색 재귀함수 이용
def binary_search_recur(array, target, start, end):
  if start > end:
    return None
  mid = (start + end) // 2
  if array[mid] == target:
    return mid
  elif array[mid] > target:
    return binary_search_recur(array, target, start, mid - 1)
  else: 
    return binary_search_recur(array, target, mid + 1, end)


for i in arr_m:
  if binary_search_recur(arr_n, i, 0, n - 1) == None:
    print("no", end = ' ')
  else:
    print("yes", end = ' ')
