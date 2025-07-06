N = int(input())
A = [0]

for _ in range(N):
    a = int(input())
    A.append(a)


count = 0
i = 1
for _ in range(2 * N):
    count += 1
    i = A[i]

    if i == 2:
        print(count)
        exit()

print(-1)
