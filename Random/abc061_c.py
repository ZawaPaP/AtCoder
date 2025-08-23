N, K = map(int, input().split())

nums = {}

for _ in range(N):
    a, b = map(int, input().split())
    if a not in nums:
        nums[a] = 0
    nums[a] += b

nums = sorted(nums.items())

temp = 0
for a, b in nums:
    temp += b
    if temp >= K:
        print(a)
        break
