# Advent of Code 2021 | Day 9
# Let's read the data
from day2 import read_input

data = read_input("day10.txt")

# Let's keep it simple, determine if input is valid or not
def is_valid(input_string):
    while "{}" in input_string or "[]" in input_string or "()" in input_string or "<>" in input_string:
        input_string = input_string.replace("{}", "")
        input_string = input_string.replace("[]", "")
        input_string = input_string.replace("()", "")
        input_string = input_string.replace("<>", "")
    close_count = input_string.count("}") + input_string.count("]") + input_string.count(")") + input_string.count(">")
    if close_count != 0:
        return False
    else:
        return True

for d in data:
    print(is_valid(d))

# Let's find the syntax error scores
def syntax_points(input_string):
    while "{}" in input_string or "[]" in input_string or "()" in input_string or "<>" in input_string:
        input_string = input_string.replace("{}", "")
        input_string = input_string.replace("[]", "")
        input_string = input_string.replace("()", "")
        input_string = input_string.replace("<>", "")

    point_3 = input_string.find(")") if input_string.find(")") >= 0 else 99
    point_57 = input_string.find("]") if input_string.find("]") >= 0 else 99
    point_1197 = input_string.find("}") if input_string.find("}") >= 0 else 99
    point_25137 = input_string.find(">") if input_string.find(">") >= 0 else 99

    if min(point_3, point_57, point_1197, point_25137) == point_3:
        return 3
    elif min(point_3, point_57, point_1197, point_25137) == point_57:
        return 57
    elif min(point_3, point_57, point_1197, point_25137) == point_1197:
        return 1197
    elif min(point_3, point_57, point_1197, point_25137) == point_25137:
        return 25137
    elif min(point_3, point_57, point_1197, point_25137) == 99:
        return 0
    else:
        return "Something is wrong"

total = 0
for d in data:
    if is_valid(d) == False:
        total += syntax_points(d)

print(total)