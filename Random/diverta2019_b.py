# R, G, B, N = map(int, input().split())

R, G, B, N = 13, 1, 4, 3000

count = 0
for r in range(N // R + 1):
    for g in range(N // G + 1):
        if (r * R + g * G) > N:
            continue
        if (N - (r * R + g * G)) % B == 0:
            count += 1
print(count)
