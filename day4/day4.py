from collections import defaultdict
import copy
class Solution:
    def __init__(self):
        self.numToBoard = defaultdict(list)
        self.numToBoardSets = defaultdict(list)
    def findBingo(self):
        with open('day4.txt') as f:
            arr = f.read().split('\n\n')
        randomNums = arr.pop(0)
        randomNums = randomNums.split(',')
        randomNums = list(map(lambda x: int(x), randomNums))

        for i, ele in enumerate(arr):
            bingoStr = ele.split('\n')
            bingoArr = []
            for line in bingoStr:
                line = line.split(' ')
                line = [int(n) for n in line if n != '']
                bingoArr.append(line)
            arr[i] = bingoArr
        
        def parse2D(boardNum, matrix):
            self.numToBoard[boardNum] = matrix.copy()
            n, m = len(matrix), len(matrix[0])
            row, col = set(), set()

            for i in range(n):
                for j in range(m):
                    row.add(matrix[i][j])
                    col.add(matrix[j][i])
                self.numToBoardSets[boardNum].append(row.copy())
                self.numToBoardSets[boardNum].append(col.copy())
                row.clear()
                col.clear()
            


        # Places every single set into hashmap index:list of sets
        for i, bingo in enumerate(arr):
            parse2D(i, bingo)

        #print(numToBoardSets)
        def findBoard():
            for rand in randomNums:
                for index, listSets in self.numToBoardSets.items():
                    for aSet in listSets:
                        if rand in aSet:
                            aSet.remove(rand)
                        if len(aSet) == 0:
                            return (index, rand)

        def findRowSets(board):
            return [set(line) for line in board]
        def findScore(board, num):
            total = 0
            for i in range(len(board)):
                for j in range(len(board[i])):
                    total += board[i][j]  
            return total * rand 

        def findLastBoard():
            solIndex = 0
            lastNum = 0
            for rand in randomNums:
                for index, listSets in self.numToBoardSets.items():
                    for aSet in listSets:
                        if rand in aSet:
                            aSet.remove(rand)
                        if len(aSet) == 0:
                            solIndex = index 
                            lastNum = rand
                            self.numToBoardSets[index] = {}
                            #lastSet = copy.deepcopy(self.numToBoardSets[solIndex])
            return (solIndex, lastNum)
        
        '''
        boardNum, endNum = findBoard()
        winningBoardArr = self.numToBoard[boardNum]
        winningBoardSets = [set(line) for line in winningBoardArr]
        # print(winningBoardSets)

        index = randomNums.index(endNum)
        for i in range(index + 1):
            for line in winningBoardSets:
                if randomNums[i] in line:
                    line.remove(randomNums[i])
        total = 0
        for line in winningBoardSets:
            for num in line:
                total += num
        print(total *endNum)
        '''

        
        solIndex, lastNum = findLastBoard()
        print(solIndex)
        print(lastNum)
        winningBoardArr = self.numToBoard[solIndex]
        winningBoardSets = [set(line) for line in winningBoardArr]
        index = randomNums.index(lastNum)
        print(winningBoardSets)
        for i in range(index + 1):
            for line in winningBoardSets:
                if randomNums[i] in line:
                    line.remove(randomNums[i])
        total = 0
        print(winningBoardSets)
        for line in winningBoardSets:
            for num in line:
                total += num 
        print(total * lastNum)

        
        
        


    #self.findBingo()

sol = Solution()
sol.findBingo()

