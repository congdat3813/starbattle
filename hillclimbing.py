from random import choice
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

class star:
    def __init__(self,place):
        self.place = place
        self.score = 0
        self.starArea = board[place[0]][place[1]]
def getArea(num):
    area=[]
    for i in range(5):
        for j in range(5):
            if num== board[i][j]:
                area.append([i,j])
    return area

area0=getArea(0)
area1=getArea(1)
area2=getArea(2)
area3=getArea(3)
area4=getArea(4)
arealist=[area0,area1,area2,area3,area4]

def getscore(place,starlist: list[star]):
    score=0
    for i in starlist:
        if i.place != place:
            if place[0]== i.place[0]:
                score+=1
            elif place[1]== i.place[1]:
                score+=1
            elif abs(place[0]-i.place[0])==1 and abs(place[1]-i.place[1])==1:
                score+=1
    return score

def getstarmax(starlist: list[star]):
    max=0
    n=0
    for x in starlist:
        if x.score > max:
            max=n
        n+=1
    # print(max)
    return max
def getstate(starlist: list[star]):
    state=0
    for i in starlist:
        i.score=getscore(i.place,starlist)
        state+=i.score
    return state

def getnextstate(starlist: list[star],curstate):
    startstarlist= starlist.copy()
    n=getstarmax(startstarlist)
    starArea=startstarlist[n].starArea
    nextstate=curstate
    nextstarlist= starlist.copy()
    for x in arealist[starArea]:
        nextstarlist[n].place=x
        state=getstate(nextstarlist)
        if state < nextstate:
            nextstate = state
            starlist[n].place=x
            print("a=",starlist[n].place)
        print(starlist[n].place)
    if nextstate < curstate:
        curstate=nextstate
        print(curstate)
    else:
        starlist= startstarlist.copy()
        print([starlist[i].place for i in range(5)])
    return curstate
def hillclimbing(starlist: list[star]):
    curstate= getstate(starlist)
    while curstate != 0:
        print(curstate)
        print([starlist[i].place for i in range(5)])
        curstate= getnextstate(starlist,curstate)
    print(curstate)
    print([starlist[i].place for i in range(5)])
    return starlist
starlist=[]
starlist.append(star([0,1]))
starlist.append(star([1,0]))
starlist.append(star([2,2]))
starlist.append(star([4,3]))
starlist.append(star([1,4]))
def solver():
    starlist=hillclimbing(starlist)
    for i in range(5):
        print(starlist[i].place,starlist[i].starArea,starlist[i].score)

solver()