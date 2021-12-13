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

# Seems like part two is a bit tricky, but not much
fuel_consumptions = []
for p in positions:
    fuel = sum([(abs(p - i)) * (abs(p - i) + 1) // 2 for i in positions])
    fuel_consumptions.append(fuel)

print(min(fuel_consumptions))

data = [int(x) for x in open("day7.txt").read().strip().split(",")]

pt1 = {x: sum([abs(x - z) for z in data]) for x in range(0, max(data) + 1)}
print(f"Part 1: {min(pt1.values())}")

pt2 = {
    x: sum([abs(x - z) / 2 * (2 + (abs(x - z) - 1)) for z in data])
    for x in range(0, max(data) + 1)
}
print(f"Part 2: {int(min(pt2.values()))}")
