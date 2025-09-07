T = int(input())

testcases = []
ans = []
for _ in range(T):
    a, b, c = map(int, input().split())
    # a or cが一番少ない場合、その数が答え
    if a <= b and a <= c:
        ans.append(a)
    elif c <= a and c <= b:
        ans.append(c)
    # a or cが最小ではない時、まずb回開催可能
    else:
        temp = b
        a -= b
        c -= b

        if c <= a:
            if 2 * c <= a:
                temp += c
            else:
                temp += (a + c) // 3
        elif a <= c:
            if 2 * a <= c:
                temp += a
            else:
                temp += (c + a) // 3
        ans.append(temp)

for a in ans:
    print(a)
