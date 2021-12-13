# Advent of Code 2021 | Day 1
# First things first, get the inputs from https://adventofcode.com/2021/day/1/input
import requests

link = "https://adventofcode.com/2021/day/1/input"
f = requests.get(link)
# print(f.text)

# Ah nevermind, it requires login, just copied the inputs for myself to day1.txt, will read from there
lines = []
with open("day1.txt") as f:
    lines = f.readlines()

# print(lines)

# Works just fine, but need to delete ascii characters for newlines (\n) and convert them to integers
data = []
for line in lines:
    line = int(line.replace("\n", ""))
    data.append(line)

# print(data)

# Great, as the data processing finished, now we can safely start to code to find the increases in data
current = None
increase = 0
decrease = 0

for d in data:
    # Since the current is None, we need to handle that TypeError with try except
    try:
        if d > current:
            increase += 1
        else:
            decrease += 1
        current = d
    except TypeError:
        increase = 0
        current = d

# Print out the results and submit the value of increase!
print(len(data))
print(increase)
print(decrease)

# Oh there is part two, okay the data is the same, we need to iterate in chunks of 3
chunk_sums = []
for i in range(len(data)):
    chunks = data[i : i + 3]

    if len(chunks) == 3:
        chunk_sums.append(sum(chunks))

# print(chunk_sums)

# We need to count the increases again as in part 1, it is best to turn it into a function
def increase_counter(data):
    current = None
    count = 0

    for d in data:
        try:
            if d > current:
                count += 1
            current = d
        except TypeError:
            count = 0
            current = d

    return count


# Call it with original data to make sure it works as the same and call it also for chunks for answer
print(increase_counter(data))
print(increase_counter(chunk_sums))
