import numpy as np
from statistics import mean
n=int(input('type the row you want to take the mean of'))
a=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(mean(a[n-1,:]))
