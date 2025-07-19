S = list(input())

ans = []
temp = []
count = 0

for i in range(len(S)):
    if S[i] == "#":
        count += 1
        temp.append(i + 1)
    if count == 2:
        count = 0
        ans.append(temp)
        temp = []


for a in ans:
    ans_str = ""
    ans_str += str(a[0])
    ans_str += ","
    ans_str += a[1]
    print(ans_str)
