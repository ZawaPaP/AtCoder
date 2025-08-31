N = int(input())
S = [input() for _ in range(N)]

xy = list(input().split())

if S[int(xy[0]) - 1] == xy[1]:
    print("Yes")
else:
    print("No")
