L, R = map(int, input().split())

ans = 0
l_i = 0
r_i = 0
if L <= 295:
    l_i = 0
elif L <= 416:
    l_i = 1
else:
    l_i = 2

if R <= 295:
    r_i = 0
elif R <= 416:
    r_i = 1
else:
    r_i = 2

ans = r_i - l_i

print(ans)
