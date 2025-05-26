S = input()

cnt = 0
push_b_cnt = 0
for c in reversed(S):
    # 桁数を追加するため + 1
    cnt += 1
    temp = push_b_cnt % 10
    temp = int(c) - temp
    if temp < 0:
        temp += 10
    push_b_cnt += temp
    cnt += temp

print(cnt)
