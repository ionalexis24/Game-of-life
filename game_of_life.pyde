col=1
lin=1
l=20
grid=[]

def setup():
    global col
    global lin
    global grid
    size(600*2,400*2)
    col=width/l
    lin= height/l
    grid=[[0 for i in range(col)] for j in range(lin)]
    
    background(0)
    for i in range(col):
        for j in range(lin):
            grid[j][i]=floor(random(2))
    print grid
    print(col,lin)
    
def numm(grid,x,y):
    a=[0,1]
    b=[-1,0]
    sum=0
    if(x==0):
        A=a
    elif(x==lin-1):
        A=b
    else:
        A=range(-1,2)
        
    if(y==0):
        B=a
    elif(y==col-1):
        B=b
    else:
        B=range(-1,2)    
    
    for i in B:
        for j in A: ###hai sa o facem calumea
            ccol=x+j
            llin=(y+i+col)%col
            sum+=grid[ccol][llin]
    sum-=grid[x][y]
    return sum

def draw():
    global grid
    next=[[0 for i in range(col)] for j in range(lin)]
    
    background(0)
    
    for i in range(col):
        for j in range(lin):
            x=i*l
            y=j*l
            if(grid[j][i]==1):
                rect(x,y,l-1,l-1)
                stroke(0)
                
    for i in range(col):
        for j in range(lin):
            state=grid[j][i]            
            ng=numm(grid,j,i)
            if(state==0 and ng==3):
                next[j][i]=1
            elif(state==1 and (ng<2 or ng>3)):
                next[j][i]=0
            else:
                next[j][i]=state
    grid=next
    
    delay(60)
