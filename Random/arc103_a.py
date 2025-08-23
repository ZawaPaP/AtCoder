n = int(input())

V = list(map(int, input().split()))

e_nums = {}
o_nums = {}

for i in range(len(V)):
    if i % 2 == 0:
        e_nums[V[i]] = e_nums.get(V[i], 0) + 1
    else:
        o_nums[V[i]] = o_nums.get(V[i], 0) + 1

e_nums = sorted(e_nums.items(), key=lambda x: x[1], reverse=True)
o_nums = sorted(o_nums.items(), key=lambda x: x[1], reverse=True)

count = n
if e_nums[0][0] != o_nums[0][0]:
    count -= e_nums[0][1]
    count -= o_nums[0][1]
else:
    if len(e_nums) == 1 and len(o_nums) == 1:
        count = n // 2
    else:
        # どちらかを2番目に頻度の高い数にする
        option1 = n - e_nums[0][1] - (o_nums[1][1] if len(o_nums) > 1 else 0)
        option2 = n - (e_nums[1][1] if len(e_nums) > 1 else 0) - o_nums[0][1]
        count = min(option1, option2)

print(count)
