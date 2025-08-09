n = int(input())

S = [input() for _ in range(n)]

dict_count = {'a': 51, 'b': 51, 'c': 51, 'd': 51, 'e': 51, 'f': 51, 'g': 51, 'h': 51, 'i': 51, 'j': 51, 'k': 51, 'l': 51,
              'm': 51, 'n': 51, 'o': 51, 'p': 51, 'q': 51, 'r': 51, 's': 51, 't': 51, 'u': 51, 'v': 51, 'w': 51, 'x': 51, 'y': 51, 'z': 51}

alphabet = 'abcdefghijklmnopqrstuvwxyz'

for s in S:
    for c in alphabet:
        dict_count[c] = min(dict_count[c], s.count(c))

ans = ''
for c in alphabet:
    ans += c * dict_count[c]

print(ans)
