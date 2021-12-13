# Parsing Data
with open('day5.txt') as f:
    arr = f.read().splitlines()
arr = [coord.split(' -> ') for coord in arr]
for pair in arr:
    for i, coord in enumerate(pair):
        pair[i] = tuple(coord.split(','))

# Part 1 & Part 2
coordinates = [[0 for i in range(1000)] for j in range(1000)]
for coordPair in arr:
    x1, y1 = list(map(lambda x:int(x), coordPair[0]))
    x2, y2 = list(map(lambda x:int(x), coordPair[1]))
    slope = (y2 - y1) / (x2 - x1) if (x2 - x1) != 0 else None
    if x1 == x2:
        for i in range(min(y1, y2), max(y1, y2) + 1):
            coordinates[x1][i] += 1
    elif y1 == y2:
        for i in range(min(x1, x2), max(x1, x2) + 1):
            coordinates[i][y1] += 1
    # Includes part2   
    elif abs(slope) == 1.0:
        if x1 < x2:
            j = y1
            for i in range(x1, x2 + 1):
                if y1 < y2:
                    coordinates[i][j] += 1
                    j += 1
                else:
                    coordinates[i][j] += 1
                    j -= 1
        else:
            j = y2
            for i in range(x2, x1 + 1):
                if y2 > y1:
                    coordinates[i][j] += 1
                    j -= 1
                else:
                    coordinates[i][j] += 1
                    j += 1
                    
points = 0
for i in range(len(coordinates)):
    for j in range(len(coordinates[i])):
        if coordinates[i][j] >= 2:
            points += 1
print(points)


'''
def test(x1, y1, x2, y2):
    sol = []
    if x1 < x2:
        j = y1
        for i in range(x1, x2 + 1):
            if y1 < y2:
                sol.append((i, j))
                j += 1
            else:
                sol.append((i, j))
                j -= 1
    else:
        j = y2
        for i in range(x2, x1 + 1):
            if y2 > y1:
                sol.append((i, j))
                j -= 1
            else:
                sol.append((i, j))
                j += 1
    return sol
print(test(5, 5, 10, 0))
'''