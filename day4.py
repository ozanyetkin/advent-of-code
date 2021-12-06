# Advent of Code 2021 | Day 4
# Reading data gets a bit trickier, we need to split the marked numbers and boards into lists
from day2 import read_input

data = read_input("day4.txt")

marked_numbers = [int(i) for i in data[0].split(",")]
# print(marked_numbers)
board_lines = []
for i, d in enumerate(data[1:]):
    if i % 6 != 0:
        d = d.split(" ")
        while "" in d:
            d.remove("")
        board_lines.append([int(i) for i in d])

# Oh list structure will get me killed in further steps, that's for sure
boards = []
for i in range(len(board_lines)):
    boards.append(board_lines[i:i + 5])

# Now let's find the winning board, prepare yourself squid!
