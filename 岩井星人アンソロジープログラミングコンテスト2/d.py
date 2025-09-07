N = int(input())

problems = [i for i in range(1, N + 1)]
problem_scores = []

for _ in range(N):
    problem_scores.append(list(map(int, input().split())))

# problemsについて 1 ~ Nの順列を全て試す
# permは使わない


def permutations(list):
    if len(list) == 1:
        return [list]
    else:
        result = []
        for i, v in enumerate(list):
            rest = permutations(list[:i] + list[i+1:])
            for r in rest:
                perm = [v] + r
                result.append(perm)
        return result


ans = 0
for perm in permutations(problems):
    min_score = 0
    for p in perm:
        if problem_scores[p - 1][1] < min_score:
            break
        min_score = max(min_score, problem_scores[p - 1][0])
    else:
        ans += 1

print(ans)
