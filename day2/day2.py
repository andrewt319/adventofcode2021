with open('day2.txt') as f:
    arr = f.read().splitlines()

arr = list(map(lambda x: x.split(), arr))
arr = list(map(lambda x: [x[0], int(x[1])], arr))

horizontal = 0 
depth = 0

for direction, length in arr:
    if direction == 'forward':
        horizontal += length
    elif direction == 'down':
        depth += length
    elif direction == 'up':
        depth -= length
print(depth * horizontal)

horizontal = 0
depth = 0
aim = 0
for direction, length in arr:
    if direction == 'forward':
        horizontal += length
        depth += aim * length
    elif direction == 'down':
        aim += length
    elif direction == 'up':
        aim -= length
print(depth * horizontal)