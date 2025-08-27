S = input()

RLs = []
for i in range(1, len(S)):
	if S[i - 1] == "R" and S[i] == "L":
		RLs.append(i - 1)
		RLs.append(i)

st = set(RLs)
ans = [0] * len(S)

r_index = 0
l_index = 1

for i in range(len(S)):
	if r_index < len(RLs) - 1 and S[i] == 'R' and i > RLs[r_index]:
		r_index += 2
		l_index += 2
	
	if i in st:
		ans[i] += 1
		continue


	if S[i] == "R":
		if (RLs[r_index] - i) % 2 == 0:
			ans[RLs[r_index]] += 1
		else:
			ans[RLs[r_index] + 1] += 1
	else:
		if (i - RLs[l_index]) % 2 == 0:
			ans[RLs[l_index]] += 1
		else:
			ans[RLs[l_index] - 1] += 1

print(*ans)
