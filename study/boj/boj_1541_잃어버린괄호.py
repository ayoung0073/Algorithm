data = input().split('-')

result = 0
for i in data[0].split('+'):# - 가 나오기 전 문자열을, +를 기준으로 배열을 만든 후,
    result += int(i) # 각 숫자들을 더함

for i in data[1:]: # -가 나온 후 문자열을 범위로
    for j in i.split('+'): # 각 문자열을 +로 나누고, 
        result -= int(j) # 각 문자를 숫자로 바꾸고

print(result)