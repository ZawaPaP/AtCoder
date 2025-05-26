def solve(A, B, C, D):
    MOD = 998244353  # 答えを割るモジュロ値、これは素数
    MAX = A + B + C + D + 1  # 必要な前計算の最大値

    # 階乗と逆元の前計算（高速化の重要なポイント）
    # 毎回計算するのではなく、配列に保存して再利用するテクニック（メモ化）
    fact = [1] * MAX  # fact[i] = i! mod MOD
    inv_fact = [1] * MAX  # inv_fact[i] = (i!)^(-1) mod MOD（階乗の逆元）

    # 階乗の前計算: O(MAX)
    for i in range(1, MAX):
        fact[i] = (fact[i - 1] * i) % MOD

    # フェルマーの小定理を使った逆元計算: a^(p-1) ≡ 1 (mod p) より a^(p-2) ≡ a^(-1) (mod p)
    # 最大値から逆順に計算することでO(MAX)で全ての逆元を計算できる
    inv_fact[MAX - 1] = pow(fact[MAX - 1], MOD - 2, MOD)
    for i in range(MAX - 2, -1, -1):
        inv_fact[i] = (inv_fact[i + 1] * (i + 1)) % MOD

    # 組み合わせ計算用の関数: nCk = n! / (k! * (n-k)!)
    # 前計算したfactとinv_factを使うことで計算量がO(1)になる
    def comb(n, k):
        if k < 0 or k > n:
            return 0
        return fact[n] * inv_fact[k] % MOD * inv_fact[n - k] % MOD

    # メインロジック: 一番左のブドウより左にバナナがi個ある場合を全て計算
    ans = 0
    for i in range(C + 1):  # i: 左側にあるバナナの数（0からC個まで）
        # 左側の組み合わせ: A個のリンゴ、B個のオレンジ、i個のバナナを並べる方法
        # リンゴはバナナより左に必要があるため、(A+B+i)個の位置からB個のオレンジを選ぶ組み合わせになる
        left = comb(A + B + i, B)

        # 右側の組み合わせ: 残りの(C-i)個のバナナと(D-1)個のブドウを並べる方法
        # 制約がないので、全部で(C-i+D-1)個の位置から(D-1)個のブドウを選ぶ組み合わせになる
        right = comb(D - 1 + C - i, D - 1)

        # 左側と右側の組み合わせを掛け合わせて答えに加算
        ans = (ans + left * right % MOD) % MOD

    return ans


A, B, C, D = map(int, input().split())
print(solve(A, B, C, D))
