from itertools import count
from random import shuffle
from time import time
import random
class DFSChess:
    def __init__(self,n,boardArea):
        self.boardArea = boardArea
        self.solutions = []
        self.size = n
        self.state=[]
        self.historystate = []
        self.childstate = []
        self.stackchild=[]
        self.count=0
    
    def createBoard(self,n):
        board = [[0 for i in range(n)] for j in range(n)]
        return board
    
    def setBoard(self,board,state):
        for i in range(self.size):
            board[i][state[i]] = 1
    # random state ban dau        
    def randomInit(self):
        self.state= list(range(self.size))
        shuffle(self.state)
# Kiem tra so vi tri vi pham
    def point(self,state):
        # Tao board moi
        hits = 0
        board = self.createBoard(self.size)
        # Gan board moi
        self.setBoard(board,state)
        row = 0
        # Kiem tra so vi tri vi pham
        for col in self.state:
            # neu vi tri hien tai cung area voi vi tri khac thi tang so vi pham len 1
            for i,j in zip(range(row+1),state):
                if self.boardArea[row][col] == self.boardArea[i][j] and row!=i :
                    hits += 1
            # Neu vi tri hien tai cung cot voi vi tri khac thi tang so vi pham len 1
            for i in range(row-1,-1,-1):
                if board[i][col] == 1:
                    hits+=1
            # Neu vi tri hien tai co hang xom voi vi tri khac thi tang so vi pham len 1
            if  row>0 and col>0 and board[row-1][col-1] == 1:
                hits+=1
            if row>0 and col<(self.size-1) and board[row-1][col+1] == 1:
                hits+=1
            row+=1
        return hits
#kiem tra ket qua   
    def isSolution(self):
        if self.point(self.state) == 0:
            return True
        else:
            return False
# Lay cac trang thai con
    def getChild(self):
        # Tao childstate moi
        self.childstate=[]
        state=self.state.copy()
        for i in range(self.size):
            for j in range(i+1,self.size,1):
                # thuc hien swap
                state[i],state[j]=state[j],state[i]
                # Neu trang thai con khong co trong history va khong co trong stackchild thi them vao childstate
                if (state not in self.historystate) and (state not in self.stackchild):
                    self.childstate.append(state.copy())
                # thuc hien swap lai
                state=self.state.copy()
# thuc hien DFS voi stack               
    def dfssolve(self):
        # Neu stack khong rong thi thuc hien tim kiem
        while self.stackchild!=[]:
            self.count+=1
            # Neu tim thay ket qua thi tra ve ket qua
            if self.isSolution():
                self.solutions=self.state
                return self.solutions
            # Neu khong tim thay ket qua thi lay cac trang thai con
            self.getChild()
            # Them cac trang thai con vao stack
            self.stackchild=self.childstate+self.stackchild
            # Lay trang thai dau tien trong stack
            self.state=self.stackchild[0].copy()
            # Xoa trang thai dau tien trong stack
            self.stackchild=self.stackchild[1:]
            # Them trang thai vao history
            self.historystate.append(self.state)
        # Neu stack rong thi tra ve ket qua
        return self.solutions       
# Giai quyet bai toan               
    def reportDFSSolverTime(self):
        self.state=list(range(self.size))
        shuffle(self.state)
        self.historystate.append(self.state)
        self.count+=1
        if self.isSolution():
            self.solutions=self.state
            return self.state
        self.getChild()
        self.stackchild=self.childstate+self.stackchild
        self.state=self.stackchild[0].copy()
        self.historystate.append(self.state.copy())
        self.stackchild=self.stackchild[1:]
        start = time()
        a=self.dfssolve()
        end = time()
        file= open("DFSreport.txt","a")
        file.write(str(end-start)+"\t" +str(self.count)+"\n")
        file.close()
        return a   
    
    def checkrowdif(self,row):
        for i in range(self.size):
            if row>0 :
                if self.boardArea[row][i]!=self.boardArea[row-1][i]:
                    return True
        return False
# xuat ra bang ket qua   
    def write_to_file(self):
        result = open("kq.txt", "w")
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
    
        
from testcase5 import *
from testcase6 import *
from testcase8 import *
import random  
              
# dimension = int(input("Enter board dimension: "))


# if dimension == 5:
#        boardA=random.choice(board5list)
# elif dimension == 6:
#        boardA=random.choice(board6list)
# elif dimension == 8:
#        boardA=random.choice(board8list)
# print(boardA)
# chess = DFSChess(dimension,boardA)
# from time import time
# start = time()
# solution = chess.reportDFSSolverTime()
# end =time()
# board = chess.createBoard(chess.size)
# print("count:",chess.count)
# print("Solution:")
# print(solution)


# if dimension == 5:
#     for boardA in board5list:
#         boardArea = boardA
#         chess = DFSChess(dimension,boardArea)
#         solution=chess.reportDFSSolverTime()
#         kq5.append(solution.copy())
#     with open("kq5.txt","a") as file:
#         file.write(str(kq5)+"\n")
# elif dimension == 6:
#     for boardA in board6list:
#         boardArea = boardA
#         chess = DFSChess(dimension,boardArea)
#         solution=chess.reportDFSSolverTime()
#         kq6.append(solution.copy())
#     with open("kq6.txt","a") as file:
#         file.write(str(kq6)+"\n")
# elif dimension == 8:
#     for boardA in board8list:
#         boardArea = boardA
#         chess = DFSChess(dimension,boardArea)
#         solution=chess.reportDFSSolverTime()
#         kq8.append(solution.copy())
#     with open("kq8.txt","a") as file:
#         file.write(str(kq8)+"\n")
# else:
#     print("Invalid dimension")

# for i in range(10):
#     boardA=random.choice(board5list)
#     chess = DFSChess(5,boardA)
#     solution = chess.reportDFSSolverTime()

# for i in range(10):
#     boardA=random.choice(board6list)
#     chess = DFSChess(6,boardA)
#     solution = chess.reportDFSSolverTime()
    
# for i in range(10):
#     boardA=random.choice(board8list)
#     chess = DFSChess(8,boardA)
#     solution = chess.reportDFSSolverTime()

boardA=board5list[1]
chess = DFSChess(5,boardA)
solution = chess.reportDFSSolverTime()
chess.write_to_file()