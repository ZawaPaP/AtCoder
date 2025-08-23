N = int(input())

st = set()
st.add(1)

if N == 1:
    print(1)
    exit()

max_st = 1
for i in range(2, N + 1):
    if max_st > N:
        break
    max_st += i
    st.add(i)

if max_st > N:
    st.remove(max_st - N)

for num in st:
    print(num)
