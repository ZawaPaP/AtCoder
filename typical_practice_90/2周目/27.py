N = int(input())

st = set()

ans = []
for i in range(N):
    S = input()
    if S in st:
        continue
    st.add(S)
    ans.append(i + 1)

for a in ans:
    print(a)
