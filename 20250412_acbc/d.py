
N, K = map(int, input().split())

S = input()

dict_map = {}


def map_string(str):
    for i in range(len(str)):
        if not dict_map.get(i):
            dict_map[i] = str[i]
        else:
            if dict_map[i] == str[i]:
                continue
            elif dict_map[i] != '?':
                dict_map[i] = '?'


cache = {}


def dp(str, k, i, prev_symbol):
    if cache.get((str, k, i, prev_symbol)):
        return
    cache[(str, k, i, prev_symbol)] = True
    if k < 0:
        return
    if len(str) == N:
        if k == 0:
            map_string(str)
        return
    if S[i] == prev_symbol == 'o':
        return
    if S[i] == '.':
        dp(str + S[i], k, i + 1, S[i])
        return
    if S[i] == 'o':
        dp(str + S[i], k - 1, i + 1, S[i])
        return
    if k > 0 and prev_symbol != 'o':
        dp(str + 'o', k - 1, i + 1, 'o')
    dp(str + '.', k, i + 1, '.')


if S[0] == 'o':
    dp(S[0], K - 1, 1, S[0])
elif S[0] == '.':
    dp(S[0], K, 1, S[0])
else:
    dp('', K, 0, '')

print("".join(dict_map.values()))
