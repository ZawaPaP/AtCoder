N, M = map(int, input().split())

masks = []
for _ in range(M):
    mask = 0
    lst = list(map(int, input().split()))
    for i in lst[1:]:
        mask |= 1 << i - 1
    masks.append(mask)

p = list(map(int, input().split()))

ans = 0
for on_switch in range(1 << N):
    all_lit = True
    for i in range(M):
        on_count = (masks[i] & on_switch).bit_count()
        if on_count % 2 == p[i]:
            continue
        else:
            all_lit = False
            break
    if all_lit:
        ans += 1
print(ans)
