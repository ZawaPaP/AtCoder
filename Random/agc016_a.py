s = input()

char_set = set(s)

if len(char_set) == 1:
    print(0)
    exit()

longest_count = float("inf")

for char in char_set:
    char_longest_count = 0
    temp = 0
    for i in range(len(s) - char_longest_count):
        if s[i] != char:
            temp += 1
        else:
            char_longest_count = max(char_longest_count, temp)
            temp = 0
    longest_count = min(longest_count, max(char_longest_count, temp))

print(longest_count)
