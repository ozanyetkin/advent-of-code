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
        grid[start_x, start_y:end_y + 1] = np.array([i + 1 for i in grid[start_x, start_y:end_y + 1]])
        # print(grid[start_x][start_y:end_y])
    if start_y == end_y:
        # print(grid[start_x:end_x][start_y])
        grid[start_x:end_x + 1, start_y] = np.array([i + 1 for i in grid[start_x:end_x + 1, start_y]])

print(grid)
print(np.count_nonzero(grid >= 2))

# Let's check other codes
from collections import Counter
import itertools
import sys

def parse_input(input):
    vectors = []
    for line in input:
        vector = [(int(x), int(y)) for (x,y) in tuple([point.split(',') for point in line.split(" -> ")])]
        vectors.append(vector)
    
    return vectors

def vec_to_pts(vector, include_diagonals):
    ((x1, y1), (x2, y2)) = vector
    if x1 == x2:
        return [(x1, y) for y in (range(y1, y2+1) if y1<y2 else range(y2, y1+1))]
    elif y2 == y1:
        return [(x, y1) for x in (range(x1, x2+1) if x1<x2 else range(x2, x1+1))]
    elif include_diagonals:
        slope = round((y2-y1) / (x2-x1))
        intercept = y2-slope*x2
        return [(x, round(slope*x+intercept)) for x in (range(x1, x2+1) if x1<x2 else range(x2, x1+1))]
    else:
        return []
     
def find_overlap_pts(vectors, include_diagonals):
    all_points = itertools.chain(*[vec_to_pts(vector, include_diagonals) for vector in vectors])
    occurrences = Counter(all_points)
    return [(point, count) for (point, count) in occurrences.items() if count > 1]

def main():
    input = data
    vecs = parse_input(input)
    
    pt1_overlapped_points = find_overlap_pts(vecs, include_diagonals=False)
    print("Part1: {}".format(len(pt1_overlapped_points)))

    pt2_overlapped_points = find_overlap_pts(vecs, include_diagonals=True)
    print("Part2: {}".format(len(pt2_overlapped_points)))
    
if __name__ == "__main__":
        main()