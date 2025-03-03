import numpy as np

arr1=np.array([1,2,3,13,18,11])
arr2=np.array([11,13,18,16,10,9])

arr3=np.intersect1d(arr1,arr2)

print(f"The common values in both the arrays is: {arr3}")