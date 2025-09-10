S = input()
T = input()

s_to_t = {}
t_to_s = {}

for s, t in zip(S, T):
    if s in s_to_t and s_to_t[s] != t:
        print("No")
        exit()
    if t in t_to_s and t_to_s[t] != s:
        print("No")
        exit()
    s_to_t[s] = t
    t_to_s[t] = s

print("Yes")
