N = int(input())

A, B, C = map(int, input().split())

ans = 10000

for use_a in range(ans):
    for use_b in range(ans - use_a):
        use_c = (N - (A * use_a + B * use_b)) // C
        if (N - (A * use_a + B * use_b)) % C == 0 and use_c >= 0:
            ans = min(ans, use_a + use_b + use_c)

print(ans)
