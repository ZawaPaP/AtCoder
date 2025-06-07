N, L = map(int, input().split())

words = []

for _ in range(N):
    s = input()
    words.append(s)

words.sort()
ans = ""
for word in words:
    ans += word
print(ans)
