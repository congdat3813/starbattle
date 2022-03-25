from tkinter import *
from tkinter import messagebox,ttk
import tkinter as tk

win = Tk()
win.title("The Knight's Tour")
win.geometry("900x900")
win.resizable(height=False,width=False)
win.configure(bg='#e17055')
canvas = Canvas(win, width=800, height=800,bg='#e17055',highlightbackground='#e17055')

path=[0,0,0,0,0]
place=[0,0]
pathlist=[]
board=[[0,0,0,0,0],
       [1,1,0,0,2],
       [1,1,3,3,2],
       [1,1,3,3,2],
       [1,1,3,4,4]]
boardstar=[[0,0,0,0,0],
           [0,0,0,0,0],
           [0,0,0,0,0],
           [0,0,0,0,0],
           [0,0,0,0,0]]
def checkboard(a):
    for i in range(5):
        for j in range(5):
            if board[i][j]==a and boardstar[i][j]==1:
                return False
    return True    

def checkstar(place):
    for i in range(5):
        if boardstar[place[0]][i] == 1:
            return False
    for i in range(5):
        if boardstar[i][place[1]] == 1:
            return False
    if place[0]==0 and place[1]==0:
        if boardstar[place[0]+1][place[1]+1] == 1:
            return False
    elif place[0]==4 and place[1]==4:
        if boardstar[place[0]-1][place[1]-1] == 1:
            return False
    elif place[0]==0 and place[1]==4:
        if boardstar[place[0]+1][place[1]-1] == 1:
            return False
    elif place[0]==4 and place[1]==0:
        if boardstar[place[0]-1][place[1]+1] == 1:
            return False
    elif place[0]==0:
        if boardstar[place[0]+1][place[1]-1] == 1 or boardstar[place[0]+1][place[1]+1] == 1:
            return False
    elif place[0]==4:
        if boardstar[place[0]-1][place[1]-1] == 1 or boardstar[place[0]-1][place[1]+1] == 1:
            return False
    elif place[1]==0:
        if boardstar[place[0]-1][place[1]+1] == 1 or boardstar[place[0]+1][place[1]+1] == 1:
            return False
    elif place[1]==4:
        if boardstar[place[0]-1][place[1]-1] == 1 or boardstar[place[0]+1][place[1]-1] == 1:
            return False
    else:
        if boardstar[place[0]-1][place[1]-1] == 1 or boardstar[place[0]-1][place[1]+1] == 1 or boardstar[place[0]+1][place[1]-1] == 1 or boardstar[place[0]+1][place[1]+1] == 1:
            return False
    return True
def check(a,place):
    if checkboard(a) and checkstar(place):
        return True
    else:
        return False

def dfssolve(rows):
    row = rows
    for col in range(5):
        a=board[row][col]
        if check(a,[row,col]):
            path[row]=col
            boardstar[row][col]=1
            if row == 4:
                pathlist.append([path[x] for x in range(5)])
            else:
                dfssolve(row+1)
            boardstar[row][col]=0

dfssolve(0)
print(pathlist)
