N, x = map(int, input().split())
A = list(map(int, input().split()))


A.sort()

ans = 0
for i in range(N):
    if x >= A[i]:
        x -= A[i]
        ans += 1
    else:
        break

# お菓子が余っていたら1人に全部あげる
if x > 0 and ans == N:
    ans -= 1

print(ans)
