N, M = map(int, input().split())

food_variation_dic = {}
food_dic = {}

for i in range(M):
    k = list(map(int, input().split()))
    food_variation_dic[i] = k[0]
    for syokuzai in range(1, k[0] + 1):
        if k[syokuzai] in food_dic:
            food_dic[k[syokuzai]].append(i)
        else:
            food_dic[k[syokuzai]] = [i]

B = list(map(int, input().split()))

completed = set()

ans = 0
for b in B:
    if b not in food_dic:  # 存在しない食材の場合はスキップ
        print(ans)
        continue

    dishes = food_dic[b]
    for dish in dishes:
        if dish in completed:
            continue
        food_variation_dic[dish] -= 1
        if food_variation_dic[dish] == 0:
            completed.add(dish)
            ans += 1

    print(ans)
