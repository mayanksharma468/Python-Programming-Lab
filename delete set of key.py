from tkinter import Y


dct={}
r=int(input('enter the no. of key'))
for i in range(0,r):
    k=input('enter key')
    v=input('enter value')
    dct[k]=v
print(dct)
remove_key=eval(input('enter the list of key to delete'))
for i in remove_key:
    if i in dct:
        dct.pop(i)
print('after remove key',dct)
