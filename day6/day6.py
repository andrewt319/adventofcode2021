from collections import OrderedDict
from collections import defaultdict

with open("day6.txt") as f:
    arr = f.read().split(',')
arr = list(map(lambda x: int(x), arr))
'''
# Part 1
for _ in range(80):
    numAdd = 0
    for i in range(len(arr)):
        if arr[i] == 0:
            numAdd += 1
            arr[i] = 6
        else:
            arr[i] -= 1
    arr += [8] * numAdd
print("Part 1: " + str(len(arr)))
'''

hashmap = defaultdict(int)
day = 0
total = len(arr)
for fish in arr:
    nextFish = day + fish + 1
    for i in range(nextFish, 257, 7):
        hashmap[i] += 1
        total += 1

while day <= 256:
    if day in hashmap:
        nextFish = day + 8 + 1
        fishToAdd = hashmap[day]
        for i in range(nextFish, 257, 7):
            hashmap[i] += fishToAdd
            total += fishToAdd
    day += 1
print("Part 2: " + str(total))




