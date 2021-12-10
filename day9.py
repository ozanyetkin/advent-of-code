# Advent of Code 2021 | Day 9
# Let's read the data
from day2 import read_input
import numpy as np

data = read_input("day9.txt")

# Turn the data into a matrix
height_matrix = []
for d in data:
    rows = []
    for s in d:
        rows.append(int(s))
    height_matrix.append(rows)

height_matrix = np.array(height_matrix)
print(height_matrix)