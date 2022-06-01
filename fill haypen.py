import numpy as np

row,column=map(int,input().split())

a=[]
for i in range(0,row):
    b=list(input().split())
    a.append(b)
x=np.array(a,dtype=str)
centre=np.char.center(x,15,fillchar='_')
LEFT=np.char.ljust(x,15,fillchar='_')
Right=np.char.rjust(x,15,fillchar='_')
print(centre,LEFT,Right)
