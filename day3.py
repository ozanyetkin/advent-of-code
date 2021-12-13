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

# Oh part 2 seems a bit complicated, at least the loop structure is the same, let's see
def binary_digit(data, index):
    binary_list = []
    for d in data:
        binary_list.append(int(d[index]))

    winning_digit = binary_count(binary_list)
    return winning_digit


# Small test for winning binary function
list = ["1010", "1000", "1010", "1000"]
for i in range(len(list[0])):
    print(binary_digit(list, i))

# Another function to delete elements according to winning digit
def binary_remove(binary_list, index, binary_digit):
    removed_list = []
    for b in binary_list:
        if int(b[index]) == binary_digit:
            removed_list.append(b)
    return removed_list


# Small test for binary remove function
# print(binary_remove(data, 1, binary_digit(data, 0)))

# Now that we have necessary functions, we can implement the most interesting part, recursion
def oxygen_rate(data):
    for i in range(len(data[0])):
        print(len(data))
        winning_digit = binary_digit(data, i)
        if len(data) > 1:
            if winning_digit is not None:
                data = binary_remove(data, i, winning_digit)
            else:
                print("Equality occured")
                data = binary_remove(data, i, 1)
            print(winning_digit, data, i)
        else:
            break
    return data


def carbondioxide_rate(data):
    for i in range(len(data[0])):
        print(len(data))
        # Told you not to try this at home, causes a bug, never evaluates to None
        # losing_digit = int(not bool(binary_digit(data, i)))
        winning_digit = binary_digit(data, i)

        if winning_digit is not None:
            losing_digit = int(not bool(winning_digit))
        else:
            losing_digit = None

        if len(data) > 1:
            if losing_digit is not None:
                data = binary_remove(data, i, losing_digit)
            else:
                print("Equality occured")
                data = binary_remove(data, i, 0)
            print(losing_digit, data, i)
        else:
            break
    return data


# Calculate oxygen rate and carbondioxide rate, convert to base 10 and multiply for the answer
print(data)
oxygen_rate = oxygen_rate(data)[0]
carbondioxide_rate = carbondioxide_rate(data)[0]

print(oxygen_rate)
print(carbondioxide_rate)

print(int(oxygen_rate, 2) * int(carbondioxide_rate, 2))
