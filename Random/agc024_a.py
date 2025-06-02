A, B, C, K = map(int, input().split())

LIMIT = 10**18

# K が奇数の時 B - A
# K が偶数の時 A - B

if K % 2 == 1:
    ans = B - A
else:
    ans = A - B

if abs(ans) > LIMIT:
    print("Unfair")
else:
    print(ans)
