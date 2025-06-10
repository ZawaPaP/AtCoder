A, B, C, X, Y = map(int, input().split())


# A, B 1枚づつ買うには

both_price = min(A + B, C * 2)
a_price = min(A, C * 2)
b_price = min(B, C * 2)

min_slice = min(X, Y)

ans = 0
ans += both_price * min_slice

if min_slice < X:
    ans += a_price * (X - min_slice)
else:
    ans += b_price * (Y - min_slice)

print(ans)
