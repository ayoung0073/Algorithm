n = 1260
count = 0

# 큰 단위부터
coin_types = [500, 100, 50, 10]

for coin in coin_types:
    count += n // coin # 해당 화폐으로 거슬러 줄 수 있는 동전의 개수
    n %= coin # 남은 돈

print(coin)