O = input()
E = input()

password = ""

i = 0
while i < len(O) and i < len(E):
    password += O[i] + E[i]
    i += 1

if len(O) != len(E):
    password += O[-1]

print(password)
