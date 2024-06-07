from tkinter import *       # gui library
import tkinter.ttk as ttk   # gui library
import random               # random number library

# ---- > Backend - Game Ignition Program @ starting execution only
# ---- > Backend - frontend functions @ Everytime execution
# ---- > Frontend - GUI @ starting execution only

# variable declaration ==============================================================

row=10                  # No of Rows in Game       
column=10               # No of Rows in Game
totalShell=row*column   # Total No Of Shells
level=1                 # Deficulty Level of Game ,Defaultly as 1 - Easy

font1=("Consolas",12,"italic") # Set font for for Application


# Function for Setting Deficulty Level and destroy Window
def fixLevel(num):
    global level
    level=num
    MinesweeperLevel.destroy()

# =========================================   Dificulty level chooser Window GUI Code   ======================================================
MinesweeperLevel=Tk()
MinesweeperLevel.title('Minesweeper')
MinesweeperLevel.iconbitmap()
MinesweeperLevel.geometry('300x450')
MinesweeperLevel.resizable(False,False)

# Load Image for the Window
minephoto=PhotoImage(file="sourceimg/mine.png")
flagphoto=PhotoImage(file="sourceimg/flag.png")

imgFrame=Frame(MinesweeperLevel)
Label(imgFrame,image=minephoto).pack(side='right',padx=10)
Label(imgFrame,image=flagphoto).pack(side='right',padx=10)
imgFrame.pack(side='top',padx=15,pady=10)
Label(MinesweeperLevel,text="Minesweeper\nSelect Level",font=font1,justify='center').pack(side='top',padx=5)
Button(MinesweeperLevel,text='Easy',fg='green',bg='#999',font=font1,relief='solid',width=15,command=lambda:fixLevel(1)).pack(side='top',padx=15,pady=10)
Button(MinesweeperLevel,text='Medium',fg='blue',bg='#999',font=font1,relief='solid',width=15,command=lambda:fixLevel(2)).pack(side='top',padx=15,pady=10)
Button(MinesweeperLevel,text='Hard',fg='red',bg='#999',font=font1,relief='solid',width=15,command=lambda:fixLevel(3)).pack(side='top',padx=15,pady=10)
MinesweeperLevel.mainloop()


#========================== > Backend Game Window

mineValue=-1      # defalut value for mine
randomNumList=[]  # Store level chooser values
approxHigh=0      # for Store Approx numbers fill in get all as highest value

# edit the randomNumList[] to make changes
# deficult Level 1 = Easy =>   randomNumList[1,4,6] =>   count of mines fixed in the game row*column/6 = 16 or greater till end of array
# deficult Level 2 = Medium => randomNumList[3,5,2] =>   count of mines fixed in the game row*column/5 = 20 or greater till end of array
# deficult Level 3 = Hard =>   randomNumList[1,2,3,4] => count of mines fixed in the game row*column/4 = 25 or greater till end of array
def FindApproxHigh(TestList):
    approx=int(totalShell/max(TestList))
    #print('approx :',approx)
    return approx

if(level==1):
    randomNumList=[1,4,6]
    approxHigh=FindApproxHigh(randomNumList)
elif(level==2):
    randomNumList=[3,5,2]
    approxHigh=FindApproxHigh(randomNumList)
elif(level==3):
    randomNumList=[1,3,2,4]
    approxHigh=FindApproxHigh(randomNumList)



# allocate list space for storing values of mine hind --> defaultly set 0 as its value
array=[]
for m in range(totalShell):
    array.append(0)

# ======================================== Debuging purpose ========================================================
# For viewing the stored values in the array list
def printArrayValue():
    counts=0
    for m in range(row):
        for n in range(column):
            print(array[counts],"\t",end='')
            counts+=1
        print()

def PrintMainArray():
    for i in OutArray:
        print(i)

def PrintStatusArray():
    for i in StatusArray:
        print(i)


# Fix Mine in array function
#================================================================================
#  >  Get a random position for mines fixing
def randomNum():
    num=random.choice(randomNumList)
    #print(num)
    return num


#  >  Set a mine value in the positon given by random\
current_place=0
for i in range(approxHigh):
    current_place=current_place+randomNum()
    array[current_place]=mineValue

#  > Filling random values in empty space in array - if approximation shells filled with smaller random values
# use current_place value to till the end of array reached
while(current_place<totalShell):
    array[current_place]=mineValue
    current_place=current_place+randomNum()

#printArrayValue() # -> debug

#=================================================================================
# Converting a Linear Array list to 2D array list - For Easy manipulation
OutArray=[]      # Variable Allocation for Storing 2D List Array
StartIndex=0     # For Slicing Use
EndIndex=column  # For Slicing Use

for i in range(row):
    OutArray.append(array[StartIndex:EndIndex])
    StartIndex=EndIndex
    EndIndex=EndIndex+column


#PrintMainArray() # --> debuging purpose

#===================================================================================
# Hind Producing Function
MinesFixed=0              # For Storing No of Mines placed in Game
OpenedShells=row*column   # For Storing Numbers of OpenedShells in game while game playing & used for check game win or not
NoOfFlag=0                # For Storing No of Flags Placed in Game While Game play

# Check the Boundry Level for creating a hind without making errors 
def boundryCheck(a,b):
    if(a>=0 and b>=0 and a<row and b<column and OutArray[a][b]!=mineValue):
        OutArray[a][b]+=1

for i in range(row):
    for j in range(column):
        if(OutArray[i][j]==mineValue):
            MinesFixed+=1
            #print(" mine in ",i,j)
            boundryCheck(i-1,j-1)
            boundryCheck(i-1,j)
            boundryCheck(i-1,j+1)
            boundryCheck(i,j-1)
            boundryCheck(i,j+1)
            boundryCheck(i+1,j-1)
            boundryCheck(i+1,j)
            boundryCheck(i+1,j+1)

#PrintMainArray() # --> debuging purpose


#============================================================================
# Creating a array for storing Flag and Opened shell value - defaultly set space ' '
StatusArray = [[' ' for i in range(column)] for j in range(row)]


#PrintStatusArray() # -> For debuging purpose  

#==========================  Backend - Frontend  ============================
# Shows mine placed places in game When game overs
def mineShower():
    for i in range(row):
        for j in range(column):
            if(OutArray[i][j]==-1 and StatusArray[i][j]!='F'):
                exec(f'but_{i}{j}["image"]=mineimg')

# Game Over Executions
def GameOver():
    mineShower()
    for i in range(len(btn_list)):
        btn_list[i]["state"]='disable'
    Label(minesweeper,text='Game Over',font=('Consolas',15,'normal'),height=3,width=15,bg='#999',fg='red',relief='solid').place(relx=0.5,rely=0.5,anchor='center')
    Button(minesweeper,text='Exit',relief='solid',font=("consolas",15),command=lambda:GameExit()).place(relx=0.5,rely=0.6,anchor='center')

# Game Wining Executions
def GameWin():
    if(OpenedShells==MinesFixed):
        #print("Game Win")
        Label(minesweeper,text='You Win',font=('Consolas',15,'normal'),height=3,width=15,bg='#999',fg='green',relief='solid').place(relx=0.5,rely=0.5,anchor='center')
        Button(minesweeper,text='Exit',relief='solid',font=("consolas",15),command=lambda:GameExit()).place(relx=0.5,rely=0.6,anchor='center')

# Open a Shell While click the button
def OpenEvent(var,num,val_1,val_2):
    if(StatusArray[val_1][val_2]!='F' and StatusArray[val_1][val_2]!='X'):
        global OpenedShells
        OpenedShells-=1
        nearEmptyCheck(val_1,val_2)
        #print(OpenedShells)
        if(num==0):
            var["image"]=emptyimg
        elif(num==1):
            var["image"]=oneimg
        elif(num==2):
            var["image"]=twoimg
        elif(num==3):
            var["image"]=threeimg
        elif(num==4):
            var["image"]=fourimg
        elif(num==5):
            var["image"]=fiveimg
        elif(num==6):
            var["image"]=siximg
        elif(num==7):
            var["image"]=sevenimg
        elif(num==8):
            var["image"]=eightimg
        elif(num==-1):
            #print("Game Over")
            GameOver()
        StatusArray[val_1][val_2]='X'
    GameWin()
        
# Set and Remove Flag in non Opened Shell
def FlagEvent(var,val_1,val_2):
    global NoOfFlag
    if(StatusArray[val_1][val_2]=='F'):
        var["image"]=buttonimg
        StatusArray[val_1][val_2]=' '
        NoOfFlag-=1
        FlagLabel['text']=NoOfFlag
    elif(StatusArray[val_1][val_2]==' ' and StatusArray[val_1][val_2]!='X'):
        var["image"]=flagimg
        StatusArray[val_1][val_2]='F'
        NoOfFlag+=1
        FlagLabel['text']=NoOfFlag
        

# Function For Open Empty Space
def nearEmptyCheck(Check_I,Check_J):
    # Recursion for simplfy Execution
    def InBoundryPass(Pass_I,Pass_J):
        global OpenedShells
        if(Pass_I>=0 and Pass_I<row and Pass_J>=0 and Pass_J<column and OutArray[Pass_I][Pass_J]==0 and StatusArray[Pass_I][Pass_J]==' '):
            #print(Pass_I,Pass_J)
            OpenedShells-=1
            StatusArray[Pass_I][Pass_J]='X'
            exec(f'but_{Pass_I}{Pass_J}["image"]=emptyimg')
            nearEmptyCheck(Pass_I,Pass_J)
        elif(Pass_I>=0 and Pass_I<row and Pass_J>=0 and Pass_J<column and OutArray[Pass_I][Pass_J]!=0 and StatusArray[Pass_I][Pass_J]==' '):
            exec(f"OpenEvent(but_{Pass_I}{Pass_J},OutArray[Pass_I][Pass_J],Pass_I,Pass_J)")
        
    if(OutArray[Check_I][Check_J]==0):
        StatusArray[Check_I][Check_J]='X'
        exec(f'but_{Check_I}{Check_J}["image"]=emptyimg')
        #check down Index
        InBoundryPass(Check_I+1,Check_J)
        #check up Index
        InBoundryPass(Check_I-1,Check_J)
        #check right Index
        InBoundryPass(Check_I,Check_J+1)
        #check left Index
        InBoundryPass(Check_I,Check_J-1)


def GameExit():
    minesweeper.destroy()


#==========================  Frontend  ======================================
# GUI Code for Minesweeper Window
minesweeper=Tk()
minesweeper.title("Minesweepwer")
minesweeper.iconbitmap("sourceimg/mines-icon.ico")
minesweeper.resizable(False,False)

#==== imgs
minephoto=PhotoImage(file="sourceimg/mine.png")
mineimg=minephoto.subsample(2,2)
flagphoto=PhotoImage(file="sourceimg/flag.png")
flagimg=flagphoto.subsample(2,2)
buttonphoto=PhotoImage(file="sourceimg/button.png")
buttonimg=buttonphoto.subsample(2,2)
#====  nums
onephoto=PhotoImage(file="sourceimg/one.png")
oneimg=onephoto.subsample(2,2)
twophoto=PhotoImage(file="sourceimg/two.png")
twoimg=twophoto.subsample(2,2)
threephoto=PhotoImage(file="sourceimg/three.png")
threeimg=threephoto.subsample(2,2)
fourphoto=PhotoImage(file="sourceimg/four.png")
fourimg=fourphoto.subsample(2,2)
fivephoto=PhotoImage(file="sourceimg/five.png")
fiveimg=fivephoto.subsample(2,2)
sixphoto=PhotoImage(file="sourceimg/six.png")
siximg=sixphoto.subsample(2,2)
sevenphoto=PhotoImage(file="sourceimg/seven.png")
sevenimg=sevenphoto.subsample(2,2)
eightphoto=PhotoImage(file="sourceimg/eight.png")
eightimg=eightphoto.subsample(2,2)
emptyphoto=PhotoImage(file="sourceimg/empty.png")
emptyimg=emptyphoto.subsample(2,2)

#========================================
title=Frame(minesweeper,bg='royalblue')
Label(title,image=mineimg,compound='left',text="Minesweeper",font="{consolas 15 normal}",bg='royalblue',fg='white').pack()
title.pack(fill='x')
topFrame=Frame(minesweeper)
Label(topFrame,image=flagimg,text='Flags :',font=("consolas",15),compound='left').pack(side='left')
FlagLabel=Label(topFrame,text="0",font="{consolas 15 normal}")
FlagLabel.pack(side='left')
topFrame.pack(fill='x',pady=2)

#========================================
btn_list=[]  # For Storing Buttons variable created by loop
midFrame=Frame(minesweeper)
for i in range(row):
    for j in range(column):
        # exec() execute a block of code f' is used to format
        exec(f'but_{i}{j}=Button(midFrame,image=buttonimg,relief="solid",padx=10,pady=5,command=lambda:OpenEvent(but_{i}{j},OutArray[{i}][{j}],{i},{j}))')
        exec(f'but_{i}{j}.grid(row=i,column=j)')
        exec(f'but_{i}{j}.bind("<Button-3>",lambda event,val=but_{i}{j},ind_I={i},ind_J={j}:FlagEvent(val,ind_I,ind_J))')
        exec(f'btn_list.append(but_{i}{j})')
        
midFrame.pack()

minesweeper.mainloop()


#PrintStatusArray()  #--> debuging purpose
#print(btn_list)     #--> debuging purpose
#print(MinesFixed)   #--> debuging purpose
#print(OpenedShells) #--> debuging purpose
