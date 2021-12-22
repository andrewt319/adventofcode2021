from collections import defaultdict

with open("day12.txt") as f:
    arr = f.read().splitlines()

connections = defaultdict(list)
visited = set()
for pair in arr:
    pair = pair.split('-')
    if pair[1] != 'start' and pair[0] != 'end': connections[pair[0]].append(pair[1])
    if pair[0] != 'start' and pair[1] != 'end': connections[pair[1]].append(pair[0])

numPaths = [0]
def backtracking1(curr):
    if curr in visited:
        return
    elif curr == 'end':
        numPaths[0] += 1
        return
    neighbors = connections[curr]
    for neighbor in neighbors:
        if curr.islower(): visited.add(curr)
        backtracking1(neighbor)
        if curr in visited: visited.remove(curr)
    return

backtracking1('start')
print("Part 1: " + str(numPaths[0]))


numPaths[0] = 0
def backtracking2(curr, twice=None):
    if curr == 'end':
        numPaths[0] += 1
        return
    if curr in visited and not twice:
        twice = curr
    elif curr in visited and twice:
        return
    neighbors = connections[curr]
    for neighbor in neighbors:
        if curr.islower(): visited.add(curr)
        backtracking2(neighbor, twice)
        if curr in visited and curr != twice: visited.remove(curr)
    return

backtracking2('start')
print("Part 2: " + str(numPaths[0]))


