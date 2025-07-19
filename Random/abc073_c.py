N = int(input())

st = set()

for _ in range(N):
    a = int(input())
    if a in st:
        st.remove(a)
    else:
        st.add(a)

print(len(st))
