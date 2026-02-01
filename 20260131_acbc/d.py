T = int(input())


# 横並びで１段違いでないといけない。
# 移動させずにbaseに合わせる
def calculate_cost(lst):
    original_cost = sum(lst)
    n = len(lst)

    # 左からの登りは全て１段づつになる
    for i in range(1, n):
        if lst[i] > lst[i - 1] + 1:
            lst[i] = lst[i - 1] + 1

    # 右からの登りは全て１段づつとなる
    for i in range(n - 2, -1, -1):
        if lst[i] > lst[i + 1] + 1:
            lst[i] = lst[i + 1] + 1

    return original_cost - sum(lst)


for _ in range(T):
    N = int(input())
    R = list(map(int, input().split()))
    print(calculate_cost(R))
