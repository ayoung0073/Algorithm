## 구현 > 문자열 재정렬

s = input()

strs = ''
num = 0

for i in s:
  if i >= '0' and i <= '9':
    num += int(i)
  else:
    strs += i

print(''.join(sorted(strs)), end='')
print(num)
