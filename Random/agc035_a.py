N = int(input())

A = list(map(int, input().split()))

circle_A = A.copy()
circle_A.insert(0, A[-1])
circle_A.append(A[0])


print(circle_A)
for i in range(1, N):
    prev = circle_A[i - 1]
    next = circle_A[i + 1]

    if prev ^ next == circle_A[i]:
        continue
    else:
        print("No")
        exit()

print("Yes")
