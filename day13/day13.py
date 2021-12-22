with open("day13.txt") as f:
    arr = f.read().splitlines()

instructions = arr[-12:]
arr = arr[:-13]
arr = [coord.split(',') for coord in arr]
arr = [(int(x), int(y)) for y,x in arr]
coords = set(arr)

maxY = maxX = float('-inf') 
for y,x in arr:
    maxY, maxX = max(maxY, y), max(maxX, x)

paper = [['.' if (x,y) not in coords else '#' for y in range(maxX + 1)] for x in range(maxY + 1)]

coords = set(arr)
tmp = set()
lineNum = 655
for x, y in coords:
    if y > lineNum:
        distance = y - lineNum
        if (x, lineNum - distance) not in coords:
            tmp.add((x, lineNum - distance))
    else:
        tmp.add((x, y))
print("Part 1: " + str(len(tmp)))

numbers = set(list('0123456789'))
coords = set(arr)
for instruction in instructions:
    i = 1
    while instruction[-i] in numbers:
        i += 1
    lineNum = int(instruction[-(i - 1):])
    axis = instruction[-(i + 1)]
    tmp = set()
    for x, y in coords:
        if axis == 'x':
            if y > lineNum:
                distance = y - lineNum
                if (x, lineNum - distance) not in coords:
                    tmp.add((x, lineNum - distance))
            else:
                tmp.add((x, y))
        elif axis == 'y':
            if x > lineNum:
                distance = x - lineNum
                if (lineNum - distance, y) not in coords:
                    tmp.add((lineNum - distance, y))
            else:
                tmp.add((x,y))
    coords = tmp
    
sol = [[' ' for i in range(40)] for j in range(7)]
print("Part 2:")
for i in range(7):
    for j in range(40):
        if (i, j) in coords:
            sol[i][j] = 'X'
    print(sol[i])

# C A F J H Z C K    
