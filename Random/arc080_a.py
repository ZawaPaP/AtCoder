N = int(input())

A = list(map(int, input().split()))

# Aの要素を3種類に分ける
# 1. 4で割り切れるもの
# 2. 4で割れないが、2で割れるもの
# 3. 4で割れなく、2でも割れないもの

# 積が4の倍数になるのは
# t-1 x all
# t-2 x t-1 or t-2 x t-2

# 1の数がN/2以上ならYes
# 1の数がN/2未満なら、2の数 // 2  + 3の数 がN/2以上ならYes

count_1 = 0
count_2 = 0
count_3 = 0

for a in A:
    if a % 4 == 0:
        count_1 += 1
    elif a % 2 == 0:
        count_2 += 1
    else:
        count_3 += 1

if count_1 + count_2 // 2 >= N // 2:
    print("Yes")
else:
    print("No")
