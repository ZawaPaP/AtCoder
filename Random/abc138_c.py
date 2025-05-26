N = int(input())

V = list(map(int, input().split()))

while len(V) > 1:
    V.sort()

    first = V[0]
    second = V[1]

    new = (first + second) / 2

    V.append(new)
    V.pop(0)
    V.pop(0)

print(V[0])
