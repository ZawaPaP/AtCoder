x = int(input())

if x < 7:
    print(1)
    exit()

# 基本的には6, 5, 6, 5... と繰り返すことが最短の方法

count = 0

temp = x // 11
count += temp * 2

amari = x - temp * 11

if amari == 0:
    pass
elif amari <= 6:
    count += 1
else:
    count += 2

print(count)
