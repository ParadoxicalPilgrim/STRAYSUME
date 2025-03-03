import numpy as np

arr=np.array([[1,2,3],
              [4,5,6],
              [7,8,9]])

row_sum=np.cumsum(arr,axis=0)
clmn_sum=np.cumsum(arr,axis=1)

print(f"Row sum: {row_sum}")
print(f"Column sum: {clmn_sum}")