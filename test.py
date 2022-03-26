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
                if dna<5 and col>0 and board[dna+1][col-1] == 1:
                    if self.boardArea[dna][col] != self.boardArea[dna+1][col-1] :
                        hits+=1
                col+=1
            return hits
        
dimension = int(input("Enter board dimension: "))
boardA=[[0,1,1,1,2,2],
       [0,1,1,1,1,2],
       [0,3,3,3,2,2],
       [0,0,0,0,2,2],
       [0,0,5,5,2,5],
       [4,4,5,5,5,5]]
chess = GeneticChess(dimension,boardA)
from time import time
start = time()
solution = chess.utilityFunction(kq)
end =time()
# board = chess.createBoard(chess.size)
# chess.setBoard(board,solution)
print("Solution:")
print(solution)
# print("\nBoard:")
# for row in board:
#     print(row)
print(end - start)