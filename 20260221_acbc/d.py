N = int(input())
A = list(map(int, input().split()))


# dictで {x: len} みたいな xを最大値として 長さlenの部分列ができる、ということを記録しておく
#  ~ x までがつながれば、lenを追加できる

max_len = {}
st = set()
for i in range(N):
    base = A[i]
    st.add(base)
    ln = 1
    while base - 1 in st:
        if base - 1 in max_len:
            ln += max_len[base - 1]
            break
        base -= 1
        ln += 1

    max_len[base] = max(max_len.get(base, 0), ln)


print(max(max_len.values()))
