import sys 
input = sys.stdin.readline

h, w = map(int, input().split())
# block의 개수 w
blocks = list(map(int, input().split()))
answer = 0
for i in range(1, w - 1):
    left = max(blocks[:i])
    right = max(blocks[i+1:])
    val = min(left, right)
    if val > blocks[i]:
        answer += val - blocks[i]

print(answer)
