N = int(input())

S = input()

ans = 0


# o, xが1つづつあれば、その周辺の組み合わせ数を考える。
# 2つ目以降の組み合わせについては、その前に考えた組み合わせを除く

# ex. ooxo
# index 1, 2 のo,xの両側の組み合わせは2**2
# index 2, 3 のo,xの両側の組み合わせは index1のoを含まない数として1を考える


def get_first_diff_index(start_index, S):
    for i in range(start_index + 1, len(S)):
        if S[start_index] == "o":
            if S[i] != "o":
                return i
        else:
            if S[i] != "x":
                return i
    return -1  # 異なる文字が見つからない場合


first_diff_index = get_first_diff_index(0, S)
if first_diff_index == -1:
    print(0)
    exit()
# 最初の o,xの組み合わせの左側の文字と、右側の文字それぞれについて含める、含めないを考えると
left_len = first_diff_index
right_len = N - first_diff_index
ans += left_len * right_len

# 2つ目以降の組み合わせについて、
prev_index = first_diff_index
while prev_index < N - 1:
    index = get_first_diff_index(prev_index, S)
    if index == -1:
        break

    # このペアによる有効区間数
    left_positions = index - prev_index
    right_positions = N - index

    ans += left_positions * right_positions

    prev_index = index

print(ans)
