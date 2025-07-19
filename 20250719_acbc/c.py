T = int(input())

for _ in range(T):
    N = int(input())
    S = "0" + input()

    medics = [False] * (1 << N)

    # すべて空の場合
    medics[0] = True

    for i in range(1 << N):

        # falseの場合はスキップ
        if not medics[i]:
            continue

        # 薬品を1つずつ追加していく
        for j in range(N):
            if i & (1 << j):
                continue

            next_state = i | (1 << j)
            if S[next_state] == "0":
                medics[next_state] = True

    print("Yes" if medics[-1] else "No")
