N = int(input())

S = input()

MOD = 10**9 + 7

count_d = {}

for s in S:
    count_d[s] = count_d.get(s, 0) + 1

# 各アルファベットの選び方は、出現回数cとして、c + 1通りである (選ばないケースがあるため1を足す)

total = 1

for value in count_d.values():
    total *= value + 1

print((total - 1) % MOD)
