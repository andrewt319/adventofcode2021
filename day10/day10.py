
with open("day10.txt") as f:
    arr = f.read().splitlines() 

symbolToPoints = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}
hashmap = {
    ')': '(',
    '}': '{',
    '>': '<',
    ']': '['
}
total = 0
corrupted = set()
for line in arr:
    stack = []
    for c in line:
        if c in hashmap and stack and stack[-1] != hashmap[c]:
            total += symbolToPoints[c]
            corrupted.add(line)
            break
        elif c in hashmap.values():
            stack.append(c)
        else:
            stack.pop()
print("Part 1: " + str(total))
    

complements = {
    '[': ']',
    '{': '}',
    '<': '>',
    '(': ')'
}
symbolToPoints = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
}
allScores = []
for line in arr:
    if line in corrupted:
        continue
    stack = []
    for c in line:
        if c in hashmap.values():
            stack.append(c)
        else:
            stack.pop()
    stack.reverse()
    currScore = 0
    for c in stack:
        currScore = (currScore * 5) + symbolToPoints[complements[c]]
    allScores.append(currScore)
allScores.sort()
print("Part 2: " + str(allScores[len(allScores) // 2]))

