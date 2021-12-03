# Advent of Code 2021 | Day 3
# Yep, we need read_input function as expected, will import from day2
from day2 import read_input

data = read_input("day3.txt")
# print(data)

# Actually let's write a function before iterating to count whether 0 or 1 is winning
def binary_count(binary_list):
    count_zero = 0
    count_one = 0

    for b in binary_list:
        if b == 0:
            count_zero += 1
        elif b == 1:
            count_one += 1
        else:
            print("What did you give me bro, it ain't binary")

    if count_zero > count_one:
        return 0
    elif count_one > count_zero:
        return 1
    else:
        print("Seems like equality wins, it can even be the first step for world peace")

# Small test for binary count function
print(binary_count([0, 1, 1, 1]))
print(binary_count([0, 1, 0, 1]))
print(binary_count([0, 1, 0, 0]))

# We need to iterate both through each data and each string in each data
winner_binary = ""
loser_binary = ""

for i in range(len(data[0])):
    binary_list = []
    for d in data:
        binary_list.append(int(d[i]))
    
    winner_binary += str(binary_count(binary_list))
    # Below is the most weird solution for converting the 0 to 1 or vice versa, don't try this at home
    loser_binary += str(int(not bool(binary_count(binary_list))))

# Print the binary results to be converted to base 10 and multiply for the result
print(winner_binary)
print(loser_binary)

print(int(winner_binary, 2) * int(loser_binary, 2))