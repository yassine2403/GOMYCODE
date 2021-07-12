import math
newlist=[]
liste=[]
a=int(input("number of antecedants"))
for i in range (a):
    element =input("enter antecedant")
    liste.append(int(element))
    
def calculate():
    for i in range (len(liste)):
        newlist.append(math.floor((10*liste[i]/3)**0.5))
    return(newlist)
print(calculate())
        
