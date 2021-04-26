def solution(arr):
    answer = []
    comp = arr[0]
    answer.append(comp)
    for i in range(1, len(arr)):
        if arr[i] != comp:
            comp = arr[i]
            answer.append(arr[i])
    return answer


# 다른 좋은 풀이
def solution(arr):
  answer = []
  for i in arr:
      if answer[-1:] == [i]: continue #answer[-1:] 빈 배열이어도 예외 생기지 않는다.
      answer.append(i)

  return answer
