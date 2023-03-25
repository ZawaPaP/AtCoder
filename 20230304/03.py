import math
N = int(input())


#Nを成すAB組み合わせ個数
def func(N):
    if N == 1:
        return 1    
    cnt = 0
    sq = math.sqrt(N)
    for i in range(1, int(sq + 1)):
        if N == sq*sq:
            cnt += 1
        elif N % i == 0:
            cnt += 2
    print(N, cnt)
    return cnt

#Nを成すA + Bの組み合わせ個数 = N - 1
ans = 0
if N % 2 != 0:
    for i in range(1, int(N // 2 + 1)):
        ans += func(i) * func(N - i) * 2
    print(ans)
else:
    for i in range(1, N // 2):
        ans += func(i) * func(N - i) * 2
    ans += func(N // 2)**2
    print(ans)
