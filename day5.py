# Advent of Code 2021 | Day 5
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
grid = [[0] * 1000 for i in range(1001)]

for vent in vents:
    for points in vent:
        pass

print(vents)
# print(lines)