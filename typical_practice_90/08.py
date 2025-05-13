TARGET_STRING = "atcoder"
MOD = 10**9 + 7


N = int(input())
S = input()

# 'atcoder', 'tcoder', .... 'r' までそれぞれをkeyとするdictを考える
dict = {"atcoder": 0, "tcoder": 0, "coder": 0, "oder": 0, "der": 0, "er": 0, "r": 0}

for i in reversed(S):
    match i:
        case 'r':
            dict['r'] += 1
        case 'e':
            dict['er'] += dict['r']
        case 'd':
            dict['der'] += dict['er']
        case 'o':
            dict['oder'] += dict['der']
        case 'c':
            dict['coder'] += dict['oder']
        case 't':
            dict['tcoder'] += dict['coder']
        case 'a':
            dict['atcoder'] += dict['tcoder']
        case default:
            continue
print(dict['atcoder'] % MOD)
