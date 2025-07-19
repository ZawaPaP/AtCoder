N = int(input())
s = input()
t = input()


common_length = 0
for i in range(1, N + 1):
    if s[-i:] == t[:i]:
        common_length = max(common_length, i)

print(2 * N - common_length)
