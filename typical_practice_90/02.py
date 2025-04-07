
N = int(input())

if N % 2 != 0:
    exit()

# 一番左は常に `(`, 一番右は常に')'
# '(' の数 - ')' の数 が常に0以上

# つまり、 0.......1 のbitの両端以外のあり得るパターンを全て考え、Sortすれば良い

patterns = []


def generate_patterns(current, balance, depth):
    if depth == N:
        if balance == 0:
            patterns.append(current)
        return

    # '(' の数が N // 2 以下の時に末尾に追加するパターンが存在
    if balance + 1 <= N // 2:
        generate_patterns(current + [0], balance + 1, depth + 1)

    # ')' を末尾に追加するパターン
    if balance > 0:
        generate_patterns(current + [1], balance - 1, depth + 1)


generate_patterns([], 0, 0)

for pattern in patterns:
    result = ''.join('(' if bit == 0 else ')' for bit in pattern)
    print(result)
