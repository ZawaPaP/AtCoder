S = input()
K = int(input())

# 5000兆日後にどのくらい数字が増えるか
# 例えば、2は 2 > 22 > 2222 と2の累乗で増えていく
# 2**5000000000000000

for i in range(0, K):
    if S[i] != "1":
        print(S[i])
        exit()

print(S[K - 1])
