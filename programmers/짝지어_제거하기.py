from collections import deque

def solution(s):
    q = deque(s[0])
    print(q)
    for i in range(1, len(s)):
        if q and q[len(q) - 1] == s[i]:
            q.pop()
        else:
            q.append(s[i])
    if q:
        return 0
    else:
        return 1
