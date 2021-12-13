with open('day3.txt') as f:
    arr = f.read().splitlines()

n = len(arr)
gamma = ''
countZeros = [0 for i in range(12)]
countOnes = [0 for i in range(12)]

for binary in arr:
    for i, bit in enumerate(binary):
        if bit == '1':
            countOnes[i] += 1
        else:
            countZeros[i] += 1

for i in range(len(countZeros)):
    if countZeros[i] > countOnes[i]:
        gamma += '0'
    else:
        gamma += '1'

epsilon = ''
for bit in gamma:
    if bit == '1':
        epsilon += '0'
    else:
        epsilon += '1'

def convertBinary(binaryString):
    sol = 0
    power = 0
    for i in range(len(binaryString) - 1, -1, -1):
        sol += int(binaryString[i]) * (2 ** power)
        power += 1
    return sol

gammaNum = convertBinary(gamma)
epsilon = convertBinary(epsilon)
print(gammaNum * epsilon)

########################################################################

oxygenArr = arr.copy()
coArr = arr.copy()

def countOnes(oxygenArr, i):
    countOnes = 0
    countZeros = 0
    for binary in oxygenArr:
        if binary[i] == '1':
            countOnes += 1
        else:
            countZeros += 1
    return countOnes >= countZeros

def removeBinary(oxygenArr, bit, i):
    new = []
    for binary in oxygenArr:
        if binary[i] == bit:
            new.append(binary)
    return new
    
for i in range(len(oxygenArr[0])):
    if countOnes(oxygenArr, i):
        oxygenArr = removeBinary(oxygenArr, '1', i)
    else:
        oxygenArr = removeBinary(oxygenArr, '0', i)
    if len(oxygenArr) == 1:
        break

for i in range(len(coArr[0])):
    if countOnes(coArr, i):
        coArr = removeBinary(coArr, '0', i)
    else:
        coArr = removeBinary(coArr, '1', i)
    if len(coArr) == 1:
        break
    
oxygenRating = oxygenArr[0]
co2Rating = coArr[0]

oxygenRating = convertBinary(oxygenRating)
co2Rating = convertBinary(co2Rating)

print(oxygenRating * co2Rating)