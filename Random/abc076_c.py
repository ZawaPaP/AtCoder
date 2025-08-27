S = input()
T = input()

revealed_S = ""

# 部分文字列TをSの後方から探す
for i in range(len(S)):
    if (i + len(T)) > len(S):
        continue
    for j in range(i, i + len(T)):
        if S[j] == '?':
            continue
        if S[j] != T[j - i]:
            break
    else:
        if j == i + len(T) - 1 and (S[j] == T[j - i] or S[j] == '?'):
            revealed_S = S[:i] + T + S[i + len(T):]


if revealed_S == "":
    print("UNRESTORABLE")
else:
    revealed_S = list(revealed_S)
    for i in range(len(revealed_S)):
        if revealed_S[i] == '?':
            revealed_S[i] = 'a'
    revealed_S = ''.join(revealed_S)
    print(revealed_S)
