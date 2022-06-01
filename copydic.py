# we cannot directly copy dictionary one to another like dic2=dic1
# we copy() and dict()
a={}
num=int(input('enter the range'))
for i in range(0,num):
    x=input('enter key')
    y=input('enter value')
    a.update({x:y})
print(a)
b=a.copy()
print(b) 
c=dict(b)
print(c)
