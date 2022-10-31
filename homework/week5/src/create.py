#!/Users/antonincarratero/opt/anaconda3/bin/python

import numpy as np
import pandas as pd

db = pd.HDFStore('Database.h5')

index = pd.date_range('1/1/2000', periods=8)

df = pd.DataFrame(np.random.randn(8, 3), index=index, columns=['Col1', 'Col2', 'Col3'])

groups = ['A','B','C']     

i = 1    

for m in groups:

    subgroups = ['d','e','f']

    for n in subgroups:

        db.put(m + '/' + n, df, format = 'table', data_columns = True)
