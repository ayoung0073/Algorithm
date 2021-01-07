### 위에서 아래로 문제

n = int(input())
data = []
for i in range(n):
  data.append(int(input()))

data.sort(reverse=True)

for i in data:
  print(i, end = ' ')

### 성적이 낮은 순서로 학생 출력하기
n = int(input())

arr = []

def setting(data):
  return data[1]

for i in range(n):
  data = input().split()
  arr.append((data[0], int(data[1])))

arr = sorted(arr, key=setting) # 리턴 받아야함
# 답안 -> 람다
# key를 이용하여, 점수를 기준으로 정렬
arr =  sorted(arr, key=lambda student: student[1])
for i in arr:
  print(i[0], end=" ")

## 두 배열의 원소 교체
n, k = map(int, input().split())


a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort(reverse=True)

for i in range(k):
  if a[i] >= b[i]:
    continue
  else:
    a[i], b[i] = b[i], a[i]


print(sum(a)) # sum 내장 함수 이용
