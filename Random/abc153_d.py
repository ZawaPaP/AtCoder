H = int(input())

temp = 1
count = 1

while temp <= H:
    temp *= 2
    count += 1

ans = 2 ** (count - 1) - 1

print(ans)
