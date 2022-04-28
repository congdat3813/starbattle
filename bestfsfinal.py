from random import shuffle
import random

import tracemalloc

class BestChess:
    def __init__(self,n,boardArea,state):
        self.board = self.createBoard(n)
        self.boardArea = boardArea
        self.solutions = []
        self.size = n
        self.state= state
        self.historystate = []
        self.pointChild = []
        self.childstate = []
        self.count=0
    
    def createBoard(self,n):
        board = [[0 for i in range(n)] for j in range(n)]
        return board
    
    def setBoard(self,board,state):
        for i in range(self.size):
            board[i][state[i]] = 1

    # them state vao historystate
    def appendState(self,state):
        self.historystate.append(state)
    # Ham tinh diem cua state
    def point(self,state):
        hits = 0
        board = self.createBoard(self.size)
        self.setBoard(board,state)
        row = 0
        for col in self.state:
            for i,j in zip(range(row+1),state):
                if self.boardArea[row][col] == self.boardArea[i][j] and row!=i :
                    hits += 1
            # for i in range(row-1,-1,-1):
            #     if board[i][col] == 1:
            #         hits+=1
            if  row>0 and col>0 and board[row-1][col-1] == 1:
                hits+=1
            if row>0 and col<(self.size-1) and board[row-1][col+1] == 1:
                hits+=1
            row+=1
        return hits
    # Ham tim state con co diem nho nhat
    def getminstate(self):
        state = self.state.copy()
        for i in range(self.size):
            for j in range(i+1,self.size,1):
                state[i], state[j]= state[j], state[i]
                if state in self.historystate:
                    state=self.state.copy()
                    continue
                else:
                    self.pointChild.append(self.point(state))
                    self.childstate.append(state.copy())
                    state=self.state.copy()
        self.state=self.childstate[self.pointChild.index(min(self.pointChild))]
        self.pointChild.clear()
        self.childstate.clear()
   # Thuc hien giai thuat BestFS 
    def solve(self):
        self.appendState(self.state)
        if self.point(self.state) == 0:
            self.solutions=self.state
            return self.solutions
        else:
            while self.point(self.state) != 0:
                self.count+=1
                self.getminstate()
                self.appendState(self.state)
                if self.point(self.state) == 0:
                    self.solutions=self.state
                    return self.solutions
            return None
        
    def checkrowdif(self,row):
        for i in range(self.size):
            if row>0 :
                if self.boardArea[row][i]!=self.boardArea[row-1][i]:
                    return True
        return False
    # Xuat ket qua
    def write_to_file(self):
        result = open("kqbest.txt", "w")
        board=self.createBoard(self.size)
        self.setBoard(board,self.state)
        s=""
        import numpy as np
        table = np.full((self.size,self.size), ".")
        for i in range(self.size):
            table[i][self.state[i]] = "S"
        for i in range(self.size):
            if i ==0:
                for j in range(self.size):
                    s+="__"
                s+="\n"
                    
            if self.checkrowdif(i):
                for k in range(self.size):
                    if k==0:
                        s+="|"
                    if self.boardArea[i][k]!=self.boardArea[i-1][k]:
                        s+="__"
                    else:
                        s+="  "
                s+="\n"
            for j in range(self.size):
                if j==0:
                    s+="|"
                s+= str(table[i][j])
                if j<self.size-1 and self.boardArea[i][j]!=self.boardArea[i][j+1]:
                    s+="|"
                else:
                    if j==self.size-1:
                        s+="|"
                    s+=" "
                    
            s+="\n"
        for i in range(self.size):
            s+="__"
        result.write(s)
        result.close()
        print("Ket qua best first search: \n",s)
    # Giai quyet bai toan
    def reportbestfsSolverTime(self):
        from time import time
        start = time()
        tracemalloc.start()
        a=self.solve()
        current, peak = tracemalloc.get_traced_memory()
        end = time()
        file= open("bestreport.txt","a")
        file.write(str(end-start)+ "\t"+ str(self.count)+ "\t"+ str(current/10**6)+"MB"+"\t"+str(peak/10**6)+"MB"+"\n")
        file.close()
        tracemalloc.stop()
        return a 
    