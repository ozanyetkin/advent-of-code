# Advent of Code 2021 | Day 9
# Let's read the data
from day2 import read_input
import numpy as np
import math

data = read_input("day9.txt")

# Turn the data into a matrix
height_matrix = []
for d in data:
    rows = []
    for s in d:
        rows.append(int(s))
    height_matrix.append(rows)

height_matrix = np.array(height_matrix)
print(height_matrix.size)

# Find the low points, give 10 if adjacent is not present
low_points = []
low_ids = []
for i in range(100):
    for j in range(100):
        current = height_matrix[i, j]

        up = height_matrix[i - 1, j] if i > 0 else 10
        down = height_matrix[i + 1, j] if i < 99 else 10
        left = height_matrix[i, j - 1] if j > 0 else 10
        right = height_matrix[i, j + 1] if j < 99 else 10

        if current < min(up, down, left, right):
            low_points.append(current)
            low_ids.append((i,j))

print(sum([h + 1 for h in low_points]))
print(low_ids)

sink_sizes = []
for id in low_ids:
    i, j = id[0], id[1]
    x, y, z, t = 0, 0, 0, 0

    up = height_matrix[i - x, j] if i > 0 else 10
    down = height_matrix[i + y, j] if i < 99 else 10
    left = height_matrix[i, j - z] if j > 0 else 10
    right = height_matrix[i, j + t] if j < 99 else 10

    sink = []

    while up < 9:
        sink.append(up)
        x += 1
        up = height_matrix[i - x, j] if i > 0 else 10
    
    while down < 9:
        sink.append(down)
        y += 1
        try:
            down = height_matrix[i + y, j] if i < 99 else 10
        except IndexError:
            down = 10
    
    while left < 9:
        sink.append(left)
        z += 1
        left = height_matrix[i, j - z] if j > 0 else 10
    
    while right < 9:
        sink.append(right)
        t += 1
        try:
            right = height_matrix[i, j + t] if j < 99 else 10
        except IndexError:
            right = 10

    sink_sizes.append(len(sink))

sink_sizes.sort()
print(sink_sizes)