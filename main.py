from graphviz import Digraph
import pandas as pd
import numpy as np
df = pd.read_csv("2017-5-5.csv")
users= df.user.unique()

dictionary={}
for i in users:
    id_list=[]
    children=[]
    for index, row in df.iterrows():
        if row['user']==i:
            id_list.append(row['id'])
    for id in id_list:
        for index, row in df.iterrows():
            if row['parent']==id:
                children.append(row['user'])               
    dictionary[i]=children            
        
 

u = Digraph('unix', filename='unix.gv')
u.attr(size='6,6')
u.node_attr.update(color='lightblue2', style='filled')

for each in dictionary:
    for val in dictionary[each]:
        u.edge(str(val),str(each))

u.view()