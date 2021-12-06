# Advent of Code 2021 | Day 4
# Reading data gets a bit trickier, we need to split the marked numbers and boards into lists
from day2 import read_input

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
for board in boards:
    for number in numbers:
        winner = False
        board = mark_board(board, number)
        winner = winning_board(board)
        print(board, winner)

        if winner == True:
            print(board, winner, number)
            total = 0
            for b in board:
                for n in b:
                    if isinstance(n, int):
                        total += n
            print(number * total)
            break

# Oh my, code works but seems like I can not detect the first winner, told that list structure would drive me crazy