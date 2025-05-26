from functools import lru_cache

T = int(input())

cases = []

for _ in range(T):
    case_N = int(input())
    a = tuple(int(input()) for _ in range(2 * case_N))
    cases.append((case_N, a))


@lru_cache(maxsize=None)
def dp(i, N, A, score, left_parentless_count, right_parentless_count):
    # 終了条件
    if i >= 2 * N:
        if left_parentless_count == right_parentless_count:
            return score
        else:
            return 0

    # 残り右かっこのみ
    if left_parentless_count >= N:
        return score

    # 絶対に左かっこ
    if left_parentless_count == right_parentless_count:
        return dp(
            i + 1,
            N,
            A,
            score + A[i],
            left_parentless_count + 1,
            right_parentless_count,
        )

    # かっこの置き方
    return max(
        dp(
            i + 1,
            N,
            A,
            score + A[i],
            left_parentless_count + 1,
            right_parentless_count,
        ),
        dp(i + 1, N, A, score, left_parentless_count, right_parentless_count + 1),
    )


for N, A in cases:
    result = dp(0, N, A, 0, 0, 0)
    print(result)
