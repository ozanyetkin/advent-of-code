# Advent of Code 2021 | Day 5
import numpy as np
from day2 import read_input

data = read_input("day5.txt")
lines = [d.split(" -> ") for d in data]

# Let's roll into the raw data and make it a data structure
vents = []
for l in lines:
    points = []
    for p in l:
        # print(p.split(","))
        point = p.split(",")
        # print(point)
        x, y = int(point[0]), int(point[1])
        # print([(start_x, start_y), (end_x, end_y)])
        points.append((x, y))
    vents.append(points)
        
# Construct the grid to be increased where there is a vent passing through
grid = np.array([[0] * 1000 for i in range(1000)])

# Mark the grid iterating only the vents (do not go to points, we need it as a line)
for vent in vents:
    start_x = vent[0][0]
    end_x = vent[1][0]
    start_y = vent[0][1]
    end_y = vent[1][1]

    if start_x == end_x:
        # print(grid[start_x][start_y:end_y])
        grid[start_x, start_y:end_y] = np.array([i + 1 for i in grid[start_x, start_y:end_y]])
        # print(grid[start_x][start_y:end_y])
    if start_y == end_y:
        # print(grid[start_x:end_x][start_y])
        grid[start_x:end_x, start_y] = np.array([i + 1 for i in grid[start_x:end_x, start_y]])

print(grid)
print(np.count_nonzero(grid >= 2))