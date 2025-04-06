N = int(input())

names = set()
count = 0
ans = []

for i in range(N):
    S = input()
    names.add(S)
    if len(names) > count:
        count += 1
        ans.append(i + 1)

for day in ans:
    print(day)
