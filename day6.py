# Advent of Code 2021 | Day 6
# Oh this is a bit though, but at least data parsing is very easy
from day2 import read_input

data = read_input("day6.txt")[0].split(",")
timers = [int(d) for d in data]

print(timers)

# Seems like we need a class for lanternfish, but let's try a function first
def lanternfish(timer):
    if timer == 0:
        timers.append(8)
        timer = 6
    else:
        timer -= 1
    return timer

# Can't be that easy, let's try for 80 days loop
for i in range(80):
    for timer in timers:
        lanternfish(timer)

print(timers)

# Yep, definitely not that easy, let's create a class
class Lanternfish:
    def __init__(self, timer=8):
        self._timer = timer
    
    def next(self):
        if self._timer == 0:
            self._timer = 6
            return Lanternfish()
        else:
            self._timer -= 1

# You know what, we can handle with a function actually, let's try again
def lanternfish(index, fish_list):
    if fish_list[index] == 0:
        fish_list.append(8)
        fish_list[index] = 6
    else:
        fish_list[index] -= 1
    return fish_list

for i in range(len(timers)):
    lanternfish(i, timers)

print(len(timers))

# Actually, let's write a solver
def solve(data, days):
    tracker = [data.count(i) for i in range(9)]
    for day in range(days):
        tracker[(day + 7) % 9] += tracker[day % 9]
    return sum(tracker)


data = [int(x) for x in open("day6.txt").read().strip().split(",")]
print(f"Part 1: {solve(data, 80)}")
print(f"Part 2: {solve(data, 256)}")