N, K = map(int, input().split())

A = list(map(int, input().split()))

# スライディングウィンドウを使って、K種類以下の要素からなる最大長さを見つける

left = 0
right = 0
counter = {}  # 各要素の出現回数を記録
kinds = 0  # 現在の種類数
ans = 0

while right < N:
    # 右側のポインタを進める
    if A[right] not in counter:
        counter[A[right]] = 0
        kinds += 1
    counter[A[right]] += 1

    # 種類数がKを超えたら左側のポインタを進める
    while kinds > K:
        counter[A[left]] -= 1
        if counter[A[left]] == 0:
            del counter[A[left]]
            kinds -= 1
        left += 1

    # 現在のウィンドウサイズを答えに反映
    ans = max(ans, right - left + 1)
    right += 1

print(ans)
