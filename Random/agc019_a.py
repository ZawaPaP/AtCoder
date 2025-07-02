Q, H, S, D = map(int, input().split())
N = int(input())

# 2L買う最小金額
min_1L = min(Q * 4, H * 2, S)

min_2L = min(min_1L * 2, D)

temp = N // 2
ans = temp * min_2L

if N % 2 == 1:
    ans += min_1L

print(ans)
