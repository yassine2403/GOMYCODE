import pandas as pd
import numpy as np
dict1={'Success':[]}

exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes'],
'labels' : ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']}

df=pd.DataFrame(exam_data,)

print(df.iloc[:, 0:2])



l=['Suresh',15.5,1,'yes','k']
serie=pd.Series(l,index=['name','score','attempts','qualify','labels'])




new_df=df.drop(['attempts'],axis=1)
df=df.dropna()

df=df.append(serie, ignore_index=True)



for i in df.itertuples():
    if i[2]>=10:
        dict1['Success'].append(1)
    else:
         dict1['Success'].append(0)


df['success']=dict1['Success']

print(df.set_index('labels'))
df.to_csv('raw_di.csv', index=True)
import csv
with open('raw_di.csv') as file:
    c=csv.reader(file,delimiter=',')
    for i in c:
        print(type(c))
