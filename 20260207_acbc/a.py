N = int(input())

n = str(N)

st = set()
for i in n:
    st.add(i)

if len(st) == 1:
    print("Yes")
else:
    print("No")
