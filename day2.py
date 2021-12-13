# Advent of Code 2021 | Day 2
# Will just copy the inputs again and read it from day2.txt, but this time make it a function to just call
def read_input(file_name):
    lines = []
    with open(file_name) as f:
        lines = f.readlines()

    data = []
    for line in lines:
        line = line.replace("\n", "")
        data.append(line)
    return data


# Trying the function by calling, will assign it to new list to proceed
data = read_input("day2.txt")

# Function works just fine, but data needs further operations such as splitting input and separate into two lists
directions = []
distances = []
for d in data:
    d = d.split(" ")
    directions.append(d[0])
    distances.append(int(d[1]))

# print(directions)
# print(distances)

# Calculate the horizontal and vertical position in a same loop
horizontal = 0
vertical = 0
for dir, dist in zip(directions, distances):
    if dir == "forward":
        horizontal += dist
    elif dir == "up":
        vertical += dist
    elif dir == "down":
        vertical -= dist
    else:
        print("We are sinking or something")

# Print out the results and submit
print(horizontal)
print(vertical)
print(horizontal * vertical)

# Oh, in part two things get more complicated, let's try
horizontal = 0
vertical = 0
aim = 0

for dir, dist in zip(directions, distances):
    if dir == "forward":
        horizontal += dist
        vertical -= dist * aim
    elif dir == "up":
        aim -= dist
    elif dir == "down":
        aim += dist
    else:
        print("We are definitely sinking")

# Print out the results and submit
print(horizontal)
print(vertical)
print(horizontal * vertical)
