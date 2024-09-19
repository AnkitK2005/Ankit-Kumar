d=pd.DataFrame([[7,8],[9,10]],columns=['x','y'])
d2=pd.DataFrame([[11,12],[13,14]],columns=['x','y'])
d = pd.concat([d, d2], ignore_index=True)
print(d)
import pandas as pd
import numpy as np
info =np.array(['p','a','n','d','a','s'])
a=pd.Series(info)
print(a)

a=pd.Series(['java','python','c++','c#',np.nan])
a.map({'java':'core'})
print(a)

s = pd.Series(["a","b", "c"], name = "vals")
s.to_frame()

import matplotlib.pyplot as plt
emp=['parker','smith','john','william']
id=[102,104,109,114]
emp_series=pd.Series(emp)
id_series=pd.Series(id)
frame={'emp':emp_series,'id':id_series}
result=pd.DataFrame(frame)
print(result)

info={'D':[101,102,103],'department':['bse','btech','mtech']}
df=pd.DataFrame(info)
print(df)

info={'one':pd.Series([1,2,3,4,5,6],index=['a','b','c','d','e','f']),'two':pd.Series([1,2,3,4,5,6,7,8],index=['a','b','c','d','e','f','g','h'])}
d1=pd.DataFrame(info)
print(d1)
print(d1['one'])

info={'name':['vaishnavi','mahak','nikhil','pratush','navdeep'],'age':[19,18,25,24,26],'city':['delhi','mumbai','chennai','kolkata','banglore']}
d1=pd.DataFrame(info)
print(d1)

info={'one':pd.Series([1,2],index=['a','b']),'two':pd.Series([1,2,3],index=['a','b','c'])}
df=pd.DataFrame(info)
print("the data frame is:")
print(df)
print("delete the first column")
del df['one']
print(df)
print("delete the another column")
df.pop('two')
print(df)
print(df.loc['b'])

info={'stud.name':['nav','deep','veer'],'stud.id':[101,102,103],'dept':['btech','mtech','bse'],'grade':['A','B','C']}
# retrive values using dept names 
# retrieve the iloc of 2
# retrieve the id of the student 
a=pd.DataFrame(info)
print(a)
print(a['dept'])
print(a.iloc[2])
print(a['stud.id'])
print(a['stud.name'])

info={'one':pd.Series([1,2,3,4,5],index=['a','b','c','d','e']),'two':pd.Series([1,2,3,4,5,6],index=['a','b','c','d','e','f'])}
df=pd.DataFrame(info)
print(df[2:5])

d=pd.DataFrame([[7,8],[9,10]],columns=['x','y'])
d2=pd.DataFrame([[11,12],[13,14]],columns=['x','y'])
d = pd.concat([d, d2], ignore_index=True)
print(d)