import statistics

N = int(input())
X = []
Y = []

for i in range(N):
    x, y = map(int, input().split())
    X.append(x)
    Y.append(y)

# マンハッタン距離については、中央値(偶数この場合は2つの中央値の間の数)を取ればいい
# またマンハッタン距離の次元は全て独立している
# つまり、x[], y[] についてそれぞれ中央値を求めればいい

x_median = statistics.median(X)
y_median = statistics.median(Y)

dist = 0
for i in range(N):
    dist += abs(X[i] - x_median)
    dist += abs(Y[i] - y_median)

print(int(dist))
