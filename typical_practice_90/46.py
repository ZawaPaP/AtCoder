N = int(input())

CONSTANT = 46

A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

A_modulo = {}
B_modulo = {}
C_modulo = {}

for i in range(N):
    if (A[i] % CONSTANT) in A_modulo:
        A_modulo[A[i] % CONSTANT] += 1
    else:
        A_modulo[A[i] % CONSTANT] = 1
    if (B[i] % CONSTANT) in B_modulo:
        B_modulo[B[i] % CONSTANT] += 1
    else:
        B_modulo[B[i] % CONSTANT] = 1
    if (C[i] % CONSTANT) in C_modulo:
        C_modulo[C[i] % CONSTANT] += 1
    else:
        C_modulo[C[i] % CONSTANT] = 1

ans = 0
# 任意のA_modulo, B_modulo, C_moduloのkeyを足し合わせ、46になれば valueの掛け算の結果をansに追加
for key_a in A_modulo.keys():
    for key_b in B_modulo.keys():
        for key_c in C_modulo.keys():
            if (key_a + key_b + key_c) % CONSTANT == 0:
                ans += A_modulo[key_a] * B_modulo[key_b] * C_modulo[key_c]

print(ans)
