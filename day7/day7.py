from collections import defaultdict
with open("day7.txt") as f:
    arr = f.read().split(',')
arr = list(map(lambda x: int(x), arr))

'''
# Part 1:
hashmap = defaultdict(int)
maximum = max(arr)
for num in arr:
    for i in range(maximum + 1):
        fuel = abs(num - i)
        hashmap[i] += fuel

bestPos, bestFuel = float('inf'), float('inf')
for pos, fuel in hashmap.items():
    if fuel < bestFuel:
        bestPos, bestFuel = pos, fuel
print(bestFuel)
'''

# Part 2:
maximum = max(arr)
stepsToFuel = [0 for i in range(maximum + 1)]
runningSum = 0
for i in range(1, maximum + 1):
    stepsToFuel[i] = i + runningSum
    runningSum += i

posToFuel = defaultdict(int)
for num in arr:
    for i in range(maximum + 1):
        steps = abs(num - i)
        fuel = stepsToFuel[steps]
        posToFuel[i] += fuel 

bestPos, bestFuel = float('inf'), float('inf')
for pos, fuel in posToFuel.items():
    if fuel < bestFuel:
        bestPos, bestFuel = pos, fuel
print(bestFuel)