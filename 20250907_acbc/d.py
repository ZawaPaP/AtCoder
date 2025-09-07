N, K = map(int, input().split())

# Kを 2**nの葉をもつ完全二分木に変換


def to_tree(tree, num, count):
    if count == 0:
        tree.append(num)
    else:
        mid = num // 2
        to_tree(tree, mid, count - 1)
        to_tree(tree, num - mid, count - 1)


tree = []
to_tree(tree, K, N)

u = max(tree) - min(tree)
print(u)
print(*tree)
