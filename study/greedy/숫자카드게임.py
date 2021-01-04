#### ME
n, m = map(int, input().split())

arr = []

for i in range(n):
    arr.append(list(map(int, input().split())))

smallest = []
for i in range(n):
  arr[i].sort()
  smallest.append(arr[i][0])

# smallest.sort(reverse=True)
# print(smallest[0])

print(max(smallest))
  

#### ANS
n, m = map(int, input().split())

result = 0
for i in range(n):
  data = list(map(int, input().split()))
  min_value = min(data)

  result = max(min_value, result)

print(result)
