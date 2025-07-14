S = input()

KEYENCE = "keyence"

# 3パターンが考えられる
# xxxxkeyence
# keyencexxxx
# keyxxxxence

if len(S) < len(KEYENCE):
    print("NO")
    exit()

index = S.find(KEYENCE)
if index == 0 or len(S) - 7 == 0:
    print("YES")
    exit()

p = 0
for s in S:
    if s == KEYENCE[p]:
        p += 1
    else:
        remaining = 7 - p
        a = S[(len(S) - remaining) :]
        t = KEYENCE[(7 - remaining) :]
        if a == t:
            print("YES")
            exit()
        break
print("NO")
