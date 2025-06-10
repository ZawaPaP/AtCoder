N = int(input())
A = list(map(int, input().split()))

# 長さNの数列それぞれの要素について +-1の3通りがあるため、
# 全ての組み合わせは 3 ** N
# そのうち、Nこ全てが奇数になるものを求めて、全ての組み合わせから引く


combination = 1

for a in A:
    if a % 2 == 0:
        combination *= 2

print(3**N - combination)
