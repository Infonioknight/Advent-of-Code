from collections import deque

data = open("Bricks.txt", 'r').read().split('\n')
# data = open("Test.txt", 'r').read().split('\n')
bricks = [list(map(int, line.replace('~', ',').split(','))) for line in data]
bricks.sort(key=lambda x: x[2])

def overlap(a, b):
    return max(a[0], b[0]) <= min(b[3], a[3]) and max(a[1], b[1]) <= min(b[4], a[4])

for index, brick in enumerate(bricks):
    mz = 1
    for check in bricks[:index]:
        if overlap(brick, check):
            mz = max(mz, check[5] + 1)
    brick[5] -= brick[2] - mz
    brick[2] = mz
bricks.sort(key=lambda x: x[2])

supports = {i: set() for i in range(len(bricks))}
supported_by = {i: set() for i in range(len(bricks))}

for j, upper in enumerate(bricks):
    for i, lower in enumerate(bricks[:index]):
        if overlap(lower, upper) and upper[2] == lower[5] + 1:
            supports[i].add(j)
            supported_by[j].add(i)

print(supports)
print(supported_by)

counter = 0
# for i in range(len(bricks)):
#     if all(len(supported_by[j]) >= 2 for j in supports[i]):
#         counter += 1

for i in range(len(bricks)):
    q = deque(j for j in supports[i] if len(supported_by[j]) == 1)
    falling = set(q)

    while q:
        j = q.popleft()
        for k in supports[j] - falling:
            if supported_by[k] <= falling:
                falling.add(k)
                q.append(k)
    counter += len(falling) 
print(counter)




