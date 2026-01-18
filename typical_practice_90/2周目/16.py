N = int(input())
A, B, C = map(int, input().split())

ans = float('inf')

max_i = min(N // A, 9999)

for i in range(max_i + 1):

    if i >= ans:
        continue
    rem1 = N - A * i

    max_j = min(rem1 // B, 9999 - i)

    for j in range(max_j + 1):
        if i + j >= ans:
            break
        rem2 = rem1 - B * j
        if rem2 % C == 0:
            ans = min(ans, i + j + rem2 // C)

print(ans)
