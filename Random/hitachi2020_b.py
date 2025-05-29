A, B, M = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

coupons = []

for _ in range(M):
    coupon = list(map(int, input().split()))
    coupons.append(coupon)


# couponを使わない最小値段
ans = min(a) + min(b)

for coupon in coupons:
    f_index = coupon[0] - 1
    e_index = coupon[1] - 1
    amount = coupon[2]
    ans = min(ans, a[f_index] + b[e_index] - amount)

print(ans)
