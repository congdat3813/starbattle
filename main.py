from bestfsfinal import *
from dfsfinal import *

from testcase5 import *
from testcase6 import *
from testcase8 import *

def randomInit(n):
    state= list(range(n))
    shuffle(state)
    return state

def runmain(dimension,boardA):
    state= randomInit(dimension)
    chessbest = BestChess(dimension,boardA,state)
    solutionbest = chessbest.reportbestfsSolverTime()
    chessbest.write_to_file()

    chessdfs = DFSChess(dimension,boardA,state)
    solutiondfs = chessdfs.reportdfsSolverTime()
    chessdfs.write_to_file()
dimension = int(input("Chon kich thuoc ban co: "))
numboard= int(input("Chon ban co: "))
if dimension==5:
    boardA=board5list[numboard-1]
elif dimension==6:
    boardA=board6list[numboard-1]
else:
    boardA= board8list[numboard-1]
runmain(dimension,boardA)
print
    
# for i in range(10):
#     boardA=random.choice(board5list)
#     runmain(5,boardA)
    
# for i in range(10): 
#     boardB=random.choice(board6list)
#     runmain(6,boardB)
    
# for i in range(10):
#     boardC=random.choice(board8list)
#     runmain(8,boardC)


