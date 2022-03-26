'''
-------- Solving the problem using genetic algorithm----------

'''
'''Genetic Chess'''
kq=[0,5,2,4,1,3]
class GeneticChess:

    def __init__(self,n,boardArea):
        self.board = self.createBoard(n)
        self.boardArea = boardArea
        self.solutions = []
        self.size = n
        self.env = []
        self.goal = None
        self.goalIndex = -1


    def createBoard(self,n):
        board = [[0 for i in range(n)] for j in range(n)]
        return board

    def setBoard(self,board,gen):
        for i in range(self.size):
            board[gen[i]][i] = 1
    def genereteDNA(self):
        #genereates random list of length n
        from random import shuffle
        DNA = list(range(self.size))
        shuffle(DNA)
        while DNA in self.env:
            shuffle(DNA)
        return DNA
    def giaithua(self):
        n=self.size
        giai_thua = 1;
        if (n == 0 or n == 1):
            return giai_thua;
        else:
            for i in range(2, n + 1):
                giai_thua = giai_thua * i;
            return giai_thua
    def initializeFirstGenereation(self):
        for i in range(self.giaithua()):
            self.env.append(self.genereteDNA())

    def utilityFunction(self,gen):
        hits = 0
        board = self.createBoard(self.size)
        self.setBoard(board,gen)
        col = 0
        for dna in gen:
            for i,j in zip(gen,range(self.size)):
                if self.boardArea[dna][col] == self.boardArea[i][j] and dna!=i :
                    hits += 1
            for i in range(col-1,-1,-1):
                if self.boardArea[dna][col] != self.boardArea[dna][i] and board[dna][i] == 1:
                        hits+=1
                elif board[dna][i] == 1:
                    hits+=1
            if  dna>0 and col>0 and board[dna-1][col-1] == 1:
                if self.boardArea[dna][col] != self.boardArea[dna-1][col-1] :
                    hits+=1
            if dna<(self.size-1) and col>0 and board[dna+1][col-1] == 1:
                if self.boardArea[dna][col] != self.boardArea[dna+1][col-1] :
                    hits+=1
            col+=1
        return hits

    def isGoalGen(self,gen):
        if self.utilityFunction(gen) == 0:
            print("Goal found")
            return True
        return False

    def crossOverGens(self,firstGen,secondGen):
        '''Approach #1'''
        # bound = self.size//2
        # for i in range(bound):
        #     firstGen[i],secondGen[i] = secondGen[i],firstGen[i]
        '''Approach #2'''
        for i in range(1,len(firstGen)):
            if abs(firstGen[i-1] - firstGen[i])<2:
                firstGen[i],secondGen[i] = secondGen[i],firstGen[i]
            if abs(secondGen[i-1] - secondGen[i])<2:
                firstGen[i],secondGen[i] = secondGen[i],firstGen[i]
        '''App1 + App2'''
        # isSwapped = False
        # for i in range(1,len(firstGen)):
        #     if abs(firstGen[i-1] - firstGen[i])<2:
        #         isSwapped = True
        #         firstGen[i],secondGen[i] = secondGen[i],firstGen[i]
        #     if abs(secondGen[i-1] - secondGen[i])<2:
        #         isSwapped = True
        #         firstGen[i],secondGen[i] = secondGen[i],firstGen[i]
        # if not isSwapped:
        #     bound = self.size//2
        #     for i in range(bound):
        #          firstGen[i],secondGen[i] = secondGen[i],firstGen[i]


    def MutantGen(self,gen):
        '''Approach #1'''
        # bound = self.size//2
        # from random import randint as rand
        # leftSideIndex = rand(0,bound)
        # RightSideIndex = rand(bound+1,self.size-1)
        # gen[leftSideIndex],gen[RightSideIndex] = gen[RightSideIndex],gen[leftSideIndex]
        # return gen
        '''Approach #2'''
        # from random import randint as rand
        # newGen = []
        # for dna in gen:
        #     if dna not in newGen:
        #         newGen.append(dna)
        # for i in range(self.size):
        #     if i not in newGen:
        #         # newGen.insert(rand(0,len(gen)),i)
        #         newGen.append(i)
        # gen = newGen
        # return gen
        '''Approach #3'''
        # from random import randint as rand
        # newGen = []
        # for dna in gen:
        #     if dna not in newGen:
        #         newGen.append(dna)
        # for i in range(self.size):
        #     if i not in newGen:
        #         inserted = False
        #         for j in range(len(newGen)):
        #             if abs(newGen[j] - i) >=2:
        #                 newGen.insert(j,i)
        #                 inserted = True
        #         if not inserted:
        #             newGen.append(i)
        # gen = []
        # for dna in newGen:
        #     if dna not in gen:
        #         gen.append(dna)

        # return gen
        '''Approach #4'''
        bound = self.size//2
        from random import randint as rand
        leftSideIndex = rand(0,bound)
        RightSideIndex = rand(bound+1,self.size-1)
        newGen = []
        for dna in gen:
            if dna not in newGen:
                newGen.append(dna)
        for i in range(self.size):
            if i not in newGen:
                # newGen.insert(rand(0,len(gen)),i)
                newGen.append(i)

        gen = newGen
        gen[leftSideIndex],gen[RightSideIndex] = gen[RightSideIndex],gen[leftSideIndex]
        return gen


    def crossOverAndMutant(self):
        for i in range(1,len(self.env),2):
            firstGen = self.env[i-1][:]
            secondGen = self.env[i][:]
            self.crossOverGens(firstGen,secondGen)
            firstGen = self.MutantGen(firstGen)
            secondGen = self.MutantGen(secondGen)
            self.env.append(firstGen)
            self.env.append(secondGen)

    def makeSelection(self):
        #index problem
        genUtilities = []
        newEnv = []
        count=0
        for gen in self.env:
            count+=1
            print(count,gen,self.utilityFunction(gen))
            genUtilities.append(self.utilityFunction(gen))
        if min(genUtilities) == 0:
            self.goalIndex = genUtilities.index(min(genUtilities))
            self.goal = self.env[self.goalIndex]
            return self.env
        minUtil=None
        while len(newEnv)<self.size:
            minUtil = min(genUtilities)
            minIndex = genUtilities.index(minUtil)
            newEnv.append(self.env[minIndex])
            genUtilities.remove(minUtil)
            self.env.remove(self.env[minIndex])

        return newEnv

    def solveGA(self):
        self.initializeFirstGenereation()
        for gen in self.env:
            if self.isGoalGen(gen):
                print("Goal found")
                return gen
        count = 0
        while True:
            self.crossOverAndMutant()
            self.env = self.makeSelection()
            count +=1
            if self.goalIndex >= 0 :
                try:
                    print(count)
                    return self.goal
                except IndexError:
                    print(self.goalIndex)
            else:
                continue


    def reportGASolverTime(self):
        from time import time
        start = time()
        a=self.solveGA()
        end = time()
        with open("GA_report.txt","a") as file:
            file.write(str(end-start)+"\n")
        return a

