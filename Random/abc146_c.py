A, B, X = map(int, input().split())


def is_ok(n):
    return A * n + B * len(str(n)) <= X


def binary_search(ok, ng):
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    return ok


print(binary_search(0, 10 ** 9 + 1))
