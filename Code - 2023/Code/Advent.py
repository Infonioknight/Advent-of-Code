# data = open("Instructions.txt", 'r').read().split('\n')

# points = [(0, 0)]
# dirs = {"3": (-1, 0), "1": (1, 0), "2": (0, -1), "0": (0, 1)}

# b = 0

# for line in data:
#     _, _, code = line.split()
#     n = int(code[2:len(code)-2], 16)
#     dr, dc = dirs[code[-2]]
#     b += n
#     r, c = points[-1]
#     points.append((r + dr * n, c + dc * n))

# A = abs(sum(points[i][0] * (points[i - 1][1] - points[(i + 1) % len(points)][1]) for i in range(len(points)))) // 2

# i = (A - b // 2 + 1)
# print(i + b)