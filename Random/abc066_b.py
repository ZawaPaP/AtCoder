S = input()


def is_gu_moji(s):
    if len(s) % 2 != 0:
        return False

    mid = len(s) // 2
    former = s[:mid]
    latter = s[mid:]
    return former == latter


while S:
    S = S[:-2]
    if is_gu_moji(S):
        print(len(S))
        exit()
