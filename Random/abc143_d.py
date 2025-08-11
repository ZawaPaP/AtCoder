N = int(input())

L = list(map(int, input().split()))

L.sort()

count = 0
for i in range(N - 2):
    for j in range(i + 1, N - 1):
        for k in range(N - 1, j, -1):
            if L[i] + L[j] > L[k]:
                count += k - j
                break

print(count)
