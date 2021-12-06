# Advent of Code 2021 | Day 4
# Reading data gets a bit trickier, we need to split the marked numbers and boards into lists
from day2 import read_input
import numpy as np

data = read_input("day4.txt")

numbers = [int(i) for i in data[0].split(",")]
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

# Now let's create a function to detect the winning board, prepare yourself squid!
def winning_board(board):
    # You know what, let's first create a function on the fly that transposes the given marked board
    transposed = [[board[j][i] for j in range(len(board))] for i in range(len(board))]
    # print(transposed)

    winner = False
    for i in range(len(board)):
        while board[i].count(True) == len(board) or transposed[i].count(True) == len(board):
            winner = True
            break
    return winner

# Small test for winning borad function
test_boards = [[[True, False], [True, False]], [[False, False], [True, False]], [[False, False], [True, True]]]
for test in test_boards:    
    print(winning_board(test))

# It works just fine, now let's mark the boards with given numbers, actually, write a function for it
def mark_board(board, number):
    for i in range(len(board)):
        for j in range(len(board)):
            if number == board[i][j]:
                board[i][j] = True
    return board

# Small test for mark board function
test_number = 5
test_board = [[1, 2], [3, 5]]

print(mark_board(test_board, test_number))

# Great, time to call both functions to mark all and find the winning board
winner = False
for i, number in enumerate(numbers):
    for j, board in enumerate(boards):
        board = mark_board(board, number)
        winner = winning_board(board)
        # print(board, winner)

        if winner == True and len(board) == 5:
            print(board, j, winner, number, i)
            total = 0
            for b in board:
                for n in b:
                    # Oh for God's sake, why True is an instance of integer :/
                    if n is not True:
                        total += n
            print(total * number)
            boards.remove(boards[j])
            break

# Oh my, that was not very easy, now to part 2
# You know what, found some solution on reddit, let's compare
with open("day4.txt") as file:
    # Opening the file and setting up the boards as a nDimensional np.array.
    content = file.readlines()
    numbers = [int(n) for n in content[0].split(',')]
    board_list = [[int(n) for n in b.split()] for b in content[2:] if b != '\n']
    num_boards = len(board_list) // 5
    num_nums = len(numbers)
    boards = np.array(board_list).reshape((num_boards, 5, 5))

# Setting up the variables needed.
marked = np.zeros((num_boards, 5, 5), dtype=int)  # Change to 1 when marked.
boards_won = []
winning_sums = []

def mark(n):
    for z in range(num_boards):
        if z in boards_won:  # If the board has won don't bother marking.
            continue
        for y in range(5):
            for x in range(5):
                if boards[z, y, x] == n:
                    marked[z, y, x] = 1

def check_win():
    for board_index in range(num_boards):
        if board_index in boards_won:  # Don't need to check if it's already won.
            continue
        for i in range(5):
            if sum(marked[board_index, i, 0:]) == 5:  # Horizontal.
                boards_won.append(board_index)
                winning_sums.append(return_sum(board_index))
                continue  # If board has won horizontally don't need to check vertically.
            if sum(marked[board_index, 0:, i]) == 5:  # Vertical.
                boards_won.append(board_index)
                winning_sums.append(return_sum(board_index))

def return_sum(winning_index):
    not_marked = []
    for y in range(5):
        for x in range(5):
            if not marked[winning_index, y, x]:
                not_marked.append(boards[winning_index, y, x])
    return sum(not_marked) * number

# Main loop/logic.
for number in numbers:
    mark(number)
    check_win()


print(winning_sums.pop())
