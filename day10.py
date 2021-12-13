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