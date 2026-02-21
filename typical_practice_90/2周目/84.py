N = int(input())
S = list(input())

ans = 0
l = 0
r = 0

while l < N:
    st = set()
    for r in range(l, N):
        st.add(S[r])
        if len(st) == 2:
            ans += (N - r) * (r - l)
            l = r
            break
    if r == N - 1:
        break
print(ans)
