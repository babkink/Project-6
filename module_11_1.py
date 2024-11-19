import matplotlib.pyplot as plt
import numpy as np
import math

import pandas as pd
from numpy import array
from pandas.compat.numpy import np_long

from pandas import ExcelWriter

file = pd.read_excel('Book1.xlsx', sheet_name='RP_SP_TRUCKAPPROVAL')
file['Qty in CS'] = file['QTY (EA)'] / file['QTY (CS)']
unique_load_id = pd.unique(file['*LoadID'])
print(unique_load_id)
file_filtered = []
for i in range(len(unique_load_id)):
    file_fil = file[file['*LoadID'] == unique_load_id[i]].copy()
    totals = ['','','','','','','','','',file_fil['QTY (CS)'].sum(),file_fil['QTY (EA)'].sum(),
              '','',file_fil['Qty in CS'].sum()]
    file_fil.loc[len(file_fil.index)] = totals
    file_filtered.append(file_fil)
f = open('Book1 copy.xlsx', 'w')
with ExcelWriter('Book1 copy.xlsx', mode='w') as writer:
    for file in file_filtered:
        file.to_excel(writer, sheet_name=file.iat[1, 2])
f.close()

file = pd.read_excel('Book1.xlsx', sheet_name='RP_SP_TRUCKAPPROVAL', header=None)
file_np = array(file)
print(f'initial file contains {file.shape[0]} rows')
print(f'initial file contains {file.shape[1]} columns')
print(f'file header = {file_np[0]}')
n = 0
for i in file_np:
    if n > 10: break
    print(i)
    n += 1
    
y = [math.sin(i/10) for i in range(100)]
x = [j for j in range(100)]
plt.plot(x, y)
plt.show()
