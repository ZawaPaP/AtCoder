from enum import Enum


N, K = map(int, input().split())

R, S, P = map(int, input().split())

T = input()

score = 0
hands = []
for i in range(N):
    if i >= K and T[i] == T[i - K]:
        if T[i] == 'r' and hands[i - K] == 'p':
            score += 0
            hands.append('')
            continue
        elif T[i] == 's' and hands[i - K] == 'r':
            score += 0
            hands.append('')
            continue
        elif T[i] == 'p' and hands[i - K] == 's':
            score += 0
            hands.append('')
            continue
    if T[i] == 'r':
        score += P
        hands.append('p')
    elif T[i] == 's':
        score += R
        hands.append('r')
    elif T[i] == 'p':
        score += S
        hands.append('s')

print(score)
