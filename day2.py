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

print(directions)
print(distances)