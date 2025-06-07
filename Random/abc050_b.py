N = int(input())
T = list(map(int, input().split()))
M = int(input())

total = sum(T)

ans = []
for _ in range(M):
    p, x = map(int, input().split())

    time = total - T[p - 1] + x
    ans.append(time)

for a in ans:
    print(a)
