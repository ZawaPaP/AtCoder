A, B = map(int, input().split())


def is_kaibun(st):
    left_p = 0
    right_p = len(st) - 1
    while left_p < right_p:
        if st[left_p] != st[right_p]:
            return False
        else:
            left_p += 1
            right_p -= 1
    return True


ans = 0
for i in range(A, B + 1):
    if is_kaibun(str(i)):
        ans += 1

print(ans)
