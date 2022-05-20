import numpy as np 
R,C = list(map(int, input().split()))
M1 = []
M2 = []

for i in range(R):
    ele = list(map(int,input()))
    M1.append(ele)

for i in range(R):
    ele = list(map(int,input()))
    M2.append(ele)
M1 = np.array(M1)
M2 = np.array(M2)

a= np.add(M1,M2)
b= np.subtract(M1,M2)
d= np.multiply(M1,M2)
c= np.floor_divide(M1,M2)
e= np.mod(M1,M2)
f= np.power(M1,M2)

print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
