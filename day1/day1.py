with open('day1.txt') as f:
    arr = f.read().splitlines()


arr = list(map(lambda x: int(x), arr))
count = 0
for i in range(1, len(arr)):
    if arr[i] > arr[i - 1]:
        count += 1
print(count)



sum1 = sum(arr[0:3])
sum2 = sum(arr[1:4])
sol = 0
l1, l2, = 0, 1
r1, r2 = 3, 4
while r2 < len(arr):
    if sum2 > sum1:
        sol += 1
    sum1 += -arr[l1] + arr[r1]
    sum2 += -arr[l2] + arr[r2]
    l1 += 1
    l2 += 1
    r1 += 1
    r2 += 1
if sum2 > sum1:
    sol += 1
print(sol)


    