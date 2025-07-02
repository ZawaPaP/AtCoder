N = int(input())


def divisor(n):
    sq = n**0.5
    border = int(sq)
    table = []
    bigs = []
    for small in range(1, border + 1):
        if n % small == 0:
            table.append(small)
            big = n // small
            bigs.append(big)
    return table, bigs


table, bigs = divisor(N)

ans = N

for i in range(len(table)):
    temp = 0
    x = table[i]
    y = bigs[i]
    if x == 1:
        temp += y - 1
    elif y == 1:
        temp += x - 1
    else:
        temp += x + y - 2
    ans = min(ans, temp)

print(ans)
