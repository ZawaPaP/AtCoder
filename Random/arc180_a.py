N = int(input())
S = list(input())

MOD = 10**9 + 7

ans = 1

left = 0
right = 1
prev = S[0]

while right < N:
    if prev != S[right]:
        prev = S[right]
        right += 1

    else:
        if right - left > 2:
            ans *= (right - left + 1) // 2
            ans %= MOD
        left = right
        prev = S[right]
        right += 1

if right - left > 2:
    ans *= (right - left + 1) // 2

print(ans % MOD)
