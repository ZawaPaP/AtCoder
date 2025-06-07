s = input()

len_s = len(s)

a_index = -1
z_index = -1

for i in range(len_s):
    if s[i] == "A":
        a_index = i
        break

for j in reversed(range(len_s)):
    if s[j] == "Z":
        z_index = j
        break


print(z_index - a_index + 1)
