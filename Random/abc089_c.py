N = int(input())

d = {}

for _ in range(N):
    s = input()
    first_word = s[0]

    d[first_word] = d.get(first_word, 0) + 1

march = ["M", "A", "R", "C", "H"]

ans = 0
for i in range(5):
    for j in range(i + 1, 5):
        for k in range(j + 1, 5):
            if march[i] in d and march[j] in d and march[k] in d:
                ans += d[march[i]] * d[march[j]] * d[march[k]]

print(ans)
