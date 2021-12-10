# Advent of Code 2021 | Day 7
# Let's read the data
from day2 import read_input

data = read_input("day7.txt")[0].split(",")
positions = [int(d) for d in data]

print(positions)

# Here comes the first optimization problem of the challenge
fuel_consumptions = []
for p in positions:
    fuel = sum([abs(p - i) for i in positions])
    fuel_consumptions.append(fuel)

print(min(fuel_consumptions))