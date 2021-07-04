import numpy as np
a=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
x=int(input('enter a number'))

for i in a:
    for s in i:
        if s>=x:
            print(s)
        
