N, Q = map(int, input().split())

A = list(map(int, input().split()))

B = [int(input()) for _ in range(Q)]

minimum_a = min(A)
maximum_a = max(A)

sorted_A = sorted(A)
sorted_a_index = 0

x = [-1] * (max(B) + 1)
x[0] = 0
x[1] = 1

for i in range(2, len(x)):
    if sorted_a_index > len(A) - 1:
        break
    x[i] = x[i - 1] + (len(A) - sorted_a_index)

    while sorted_a_index < len(A) and sorted_A[sorted_a_index] < i:
        sorted_a_index += 1

for b in B:
    if b > maximum_a:
        print(-1)
        continue

    print(x[b])
