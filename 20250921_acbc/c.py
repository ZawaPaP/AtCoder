from collections import deque
N = int(input())

got_skills = set()
skill_graph = {}

for i in range(N):
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        got_skills.add(i + 1)
    else:
        if a not in skill_graph:
            skill_graph[a] = set()
        if b not in skill_graph:
            skill_graph[b] = set()
        skill_graph[a].add(i + 1)
        skill_graph[b].add(i + 1)

queue = deque(got_skills)

while queue:
    current_skill = queue.popleft()
    if current_skill in skill_graph:
        for next_skill in skill_graph[current_skill]:
            if next_skill not in got_skills:
                got_skills.add(next_skill)
                queue.append(next_skill)

print(len(got_skills))
