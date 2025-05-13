N, L = map(int, input().split())
K = int(input())

A = list(map(int, input().split()))

# K+1 個のピースのうち、最も短いものの長さの最大値をスコアとする


# スコアlで切り分けられるかどうかの判定
def able_to_cut(target_length):
    cuts = 0
    prev = 0
    for i in range(len(A)):
        if A[i] - prev >= target_length:
            cuts += 1
            prev = A[i]

        if cuts >= K and L - prev >= target_length:
            return True

    return False


# 二部探索で、able_to_cut() == true になる最大値を探す
left = 0
right = L
while right - left > 1:
    mid = (right + left) // 2
    if able_to_cut(mid):
        left = mid
    else:
        right = mid

print(left)
