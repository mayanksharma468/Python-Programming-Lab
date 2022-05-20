import numpy as np
ls = list(map(float, input("Enter the list").split()))
arr = np.array(ls)
print(arr[::-1])
