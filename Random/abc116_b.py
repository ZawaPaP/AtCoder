s = int(input())

A = [s]

for i in range(0, 1000000):
    if A[i] % 2 == 0:
        A.append(A[i] / 2)
    else:
        A.append(3 * A[i] + 1)


count = set()
for i in range(len(A)):
    if A[i] in count:
        print(i + 1)
        break
    else:
        count.add(A[i])
