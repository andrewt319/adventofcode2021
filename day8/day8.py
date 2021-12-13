from collections import defaultdict
from collections import Counter

with open("day8.txt") as f:
    arr = f.read().splitlines()

# Part 1
for i, line in enumerate(arr):
    newLine = line.split(' | ')
    arr[i] = newLine

count = 0
for _, output in arr:
    outputList = output.split()
    for word in outputList:
        if len(word) == 2 or len(word) == 4 \
            or len(word) == 3 or len(word) == 7:
            count += 1
print("Part 1: " + str(count))

# Part 2
total = 0
for signal, output in arr:
    lengthToWords = defaultdict(set)
    numToWord = {}
    signalList = signal.split()
    # Populate dictionary with length : set(words)
    for word in signalList:
        lengthToWords[len(word)].add(''.join(sorted(list(word))))
    
    #1
    one = lengthToWords[2].pop()
    numToWord[one] = '1'

    #4
    four = lengthToWords[4].pop()
    numToWord[four] = '4'

    #7
    seven = lengthToWords[3].pop()
    numToWord[seven] = '7'

    #8
    eight = lengthToWords[7].pop()
    numToWord[eight] = '8'

    #3
    for word in lengthToWords[5]:
        dict1 = Counter(one)
        dict2 = Counter(word)
        if dict1.items() <= dict2.items():
            three = word
            lengthToWords[5].remove(word)
            break
    numToWord[three] = '3'

    #9
    for word in lengthToWords[6]:
        dict1 = Counter(four)
        dict2 = Counter(word)
        if dict1.items() <= dict2.items():
            nine = word
            lengthToWords[6].remove(word)
            break 
    numToWord[nine] = '9'

    #5
    for word in lengthToWords[5]:
        dict1 = Counter(word)
        dict2 = Counter(nine)
        if dict1.items() <= dict2.items():
            five = word
            lengthToWords[5].remove(word)
            break
    numToWord[five] = '5'

    #2
    two = lengthToWords[5].pop()
    numToWord[two] = '2'

    #6
    for word in lengthToWords[6]:
        dict1 = Counter(five)
        dict2 = Counter(word)
        if dict1.items() <= dict2.items():
            six = word
            lengthToWords[6].remove(word)
            break
    numToWord[six] = '6'

    #0
    zero = lengthToWords[6].pop()
    numToWord[zero] = '0'
    
    # Find the decoded output
    outputList = output.split()
    currOutput = ''
    for word in outputList:
        signal = ''.join(sorted(list(word)))
        currOutput += numToWord[signal]
    total += int(currOutput)

print("Part 2: " + str(total))