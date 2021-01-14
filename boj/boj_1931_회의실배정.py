n = int(input())
array = []
for i in range(n):
  a, b = map(int, input().split())
  array.append((a, b)) # 시작과 끝나는 시간

array = sorted(array, key = lambda array : (array[1], array[0]))
# 1차 오름차순 기준 : array[1](끝나는 시간)
# 2차 오름차순 기준 : array[0](시작 시간)
# 끝나는 시간이 같을 때는, 시작 시간이 빠른 회의를 배치하는 것이 옳음

end = 0 # 회의 끝난 시간 초기화(다음 회의의 시작시간 전인지 체크)
idx = 0 # 시작 인덱스
result = 0 # 가능 회의 개수
while True:
  if idx == len(array): break
  i = array[idx]
  # 시작시간이 그 전 회의의 끝나는 시간 후인지 체크한다
  if i[0] < end: 
  # 이 경우는 시작시간이 끝나는 시간 전이므로, 해당 회의는 진행할 수 없음
  # 다음 회의 조건을 체크하기 위해 idx += 1
    idx += 1
    continue
  # 조건을 만족했을 때
  else:
    result += 1 # 회의 개수 + 1
    end = i[1] # 끝나는 시간 end에 저장
    idx += 1

print(result)
