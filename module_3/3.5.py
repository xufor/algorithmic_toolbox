n = int(input())
segments = [[x for x in map(int, input().split())] for i in range(n)]
segments.sort(key=lambda l: l[1])
answers = []
discovered = {}
for i in range(len(segments)):
    if discovered.get(i):
        continue
    x, y = segments[i]
    answers.append(y)
    for j in range(i, len(segments)):
        x1, y1 = segments[j]
        if discovered.get(j):
            continue
        elif y >= x1 and y <= y1:
            discovered[j] = True
print(len(answers))
print(' '.join(map(str, answers)))
    


