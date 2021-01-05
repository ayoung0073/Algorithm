n = int(input()) # 수열 크기
arr = list(map(int, input().split()))
x = int(input()) 

arr.sort()
count = 0
i = 0
j = n - 1
while i != j:
  plus = arr[i] + arr[j]
  if plus == x: 
    count += 1
    i += 1
  elif plus > x:
    j -= 1
  else:
    i += 1

print(count)

# 퀵소트 정렬을 이용하면 메모리 초과
# def quick_sort(array):
#   if len(array) <= 1:
#     return array
  
#   pivot = array[0]
#   tail = array[1:] # 맨앞 원소 제외 리스트

#   left_list = [x for x in tail if x <= pivot]
#   print(left_list)

#   right_list = [x for x in tail if x > pivot]
#   print(right_list)

#   return quick_sort(left_list) + [pivot] + quick_sort(right_list)

# arr = quick_sort(arr)
