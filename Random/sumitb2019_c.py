X = int(input())


simo_niketa = X % 100

min_needed = 0
if simo_niketa == 0:
    pass
elif simo_niketa < 5:
    min_needed += 1
else:
    min_needed += simo_niketa // 5
    min_needed += simo_niketa % 5

if X <= min_needed * 100:
    print(0)
else:
    print(1)
