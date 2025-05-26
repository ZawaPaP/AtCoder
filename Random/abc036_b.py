N = int(input())

S = []

for _ in range(N):
    s = list(input())
    S.append(s)

rotate = (list(row) for row in zip(*S[::-1]))

for r in rotate:
    print("".join(r))
