N = int(input())

ans = 0
# a は 1 から N の 3 乗根まで
a = 1
while a * a * a <= N:
    if N % a == 0:
        # 残りの積 M = b * c
        M = N // a
        # b は a から M の平方根まで
        b = a
        while b * b <= M:
            if M % b == 0:
                # c = M // b  (このとき自動的に b <= c になる)
                ans += 1
            b += 1
    a += 1

print(ans)
