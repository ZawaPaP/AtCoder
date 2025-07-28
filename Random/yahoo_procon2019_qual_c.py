K, A, B = map(int, input().split())


biscuits = 1
money = 0

exchange_rate = B - A

if exchange_rate <= 1 or K < A:
    biscuits += K
else:
    remaning_count = K - A + 1
    biscuits = A

    if remaning_count % 2 == 0:
        biscuits += remaning_count // 2 * exchange_rate
    else:
        # 最後にビスケットを叩いて1枚増やす
        biscuits += (remaning_count // 2) * exchange_rate + 1

print(biscuits)
