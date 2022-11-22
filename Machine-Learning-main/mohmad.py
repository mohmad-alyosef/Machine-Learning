import glob
import pandas as pd
import os
input_lok="C:\\Users\\mohmad\\Desktop\\Machine-Learning-main\\output"
df = []
for file in os.listdir(input_lok):
    if file.endswith('.xlsx'):
        print('loading file {0}...'.format(file))
        df.append(pd.read_excel(os.path.join(input_lok, file)))
len(df)
df_master = pd.concat(df,axis=0)
df_master.to_excel('C:\\Users\\mohmad\\Desktop\\Machine-Learning-main\\out\\master.xlsx', index=False)
df_master['name'] = df_master['name'].astype('category')
df_master.groupby(by='name').sum()
