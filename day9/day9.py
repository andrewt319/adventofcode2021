import heapq
with open("day9.txt") as f:
    arr = f.read().splitlines()

arr = [list(line) for line in arr]
arr = [list(map(lambda x: int(x), line)) for line in arr]

numRows, numCols = len(arr), len(arr[0])
def isValid(x, y):
    if x < 0 or x >= numRows or y < 0 or y >= numCols:
        return False
    return True

riskLevels = 0
for i in range(numRows):
    for j in range(numCols):
        north = arr[i - 1][j] if isValid(i - 1, j) else float('inf')
        west = arr[i][j - 1] if isValid(i, j - 1) else float('inf')
        south = arr[i + 1][j] if isValid(i + 1, j) else float('inf')
        east = arr[i][j + 1] if isValid(i, j + 1) else float('inf')
        curr = arr[i][j]
        if curr < north and curr < west and curr < south and curr < east:
            riskLevels += 1 + curr
print("Part 1: " + str(riskLevels))


visited = set()
pq = []
def dfs(x, y):
    if not isValid(x, y) or (x,y) in visited or arr[x][y] == 9:
        return 0
    visited.add((x, y))
    north = dfs(x - 1, y)
    west = dfs(x, y - 1)
    south = dfs(x + 1, y)
    east = dfs(x, y + 1)
    return north + west + south + east + 1

for i in range(numRows):
    for j in range(numCols):
        heapq.heappush(pq, -dfs(i, j))
basin1 = -heapq.heappop(pq)
basin2 = -heapq.heappop(pq)
basin3 = -heapq.heappop(pq)
print("Part 2: " + str(basin1 * basin2 * basin3))