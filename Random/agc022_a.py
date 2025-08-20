S = input()

REVERSE_ALPHABETS = "zyxwvutsrqponmlkjihgfedcba"

alphabets = [False] * 26


if len(S) < 26:
    for s in S:
        alphabets[ord(s) - ord("a")] = True

    for i in range(26):
        if not alphabets[i]:
            print(S + chr(i + ord("a")))
            exit()


if S == REVERSE_ALPHABETS:
    print(-1)
    exit()

# 末尾から S[i] > S[i -1]となるところを探す
for i in range(len(S) - 1, 0, -1):
    if S[i] > S[i - 1]:
        for j in range(i):
            alphabets[ord(S[j]) - ord("a")] = True

        for j in range(26):
            if not alphabets[j] and chr(j + ord("a")) > S[i - 1]:
                print(S[:i - 1] + chr(j + ord("a")))
                exit()
