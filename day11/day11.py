from collections import deque

with open("day11.txt") as f:
    arr = f.read().splitlines()

arr = [list(map(lambda x: int(x), list(nums))) for nums in arr]
arrCopy = [array.copy() for array in arr]
q = deque()
NUMROWS = 10
NUMCOLS = 10
NUMOCTOPUS = NUMROWS * NUMCOLS

def isValid(r, c):
    if r < 0 or c < 0 or r >= NUMROWS or c >= NUMCOLS:
        return False
    return True

def increment(arr):
    for i in range(NUMROWS):
        for j in range(NUMCOLS):
            arr[i][j]  = (arr[i][j] + 1) % 10
            if arr[i][j] == 0: q.append((i, j))

def bfs(arr):
    visited = set()
    count = 0 
    while len(q) != 0:
        neighbors = len(q)
        for i in range(neighbors):
            r, c = q.popleft()
            if ((r, c)) in visited:
                continue
            elif arr[r][c] == 0:
                count += 1
                visited.add((r, c))
                if isValid(r - 1, c): q.append((r - 1, c))
                if isValid(r + 1, c): q.append((r + 1, c))
                if isValid(r, c + 1): q.append((r, c + 1))
                if isValid(r, c - 1): q.append((r, c - 1))
                if isValid(r - 1, c - 1): q.append((r - 1, c - 1))
                if isValid(r - 1, c + 1): q.append((r - 1, c + 1))
                if isValid(r + 1, c + 1): q.append((r + 1, c + 1))
                if isValid(r + 1, c - 1): q.append((r + 1, c - 1))
            else:
                arr[r][c]  = (arr[r][c] + 1) % 10
                if arr[r][c] == 0: q.append((r, c))   
    return count

flashes = 0
for i in range(100):
    increment(arr)
    flashes += bfs(arr)
print("Part 1: " + str(flashes))


step = 0
while bfs(arrCopy) != NUMOCTOPUS:
    increment(arrCopy)
    step += 1
print("Part 2: " + str(step))




