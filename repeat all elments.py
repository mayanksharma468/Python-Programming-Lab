import numpy as np
lst=[['sachin','kuldeep','manish']]
b=lst.copy()
a=np.array(lst,dtype=str)
for i in range(0,2):
    for j in range(len(a)):
        for k in range(len(a[j])):
            b[j][k]+=a[j][k]
print(b)
# by char fun
new_array=np.char.multiply(a,3)
print(new_array)
