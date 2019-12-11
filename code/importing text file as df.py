import os
import pandas as pd
os.chdir(r"D:\DS_challenges\CS4003 DA Projects\CS4003 Projects\Data Set")
df = pd.DataFrame(columns=['A','B','C','D'])
i=0
with open(r'CANCER.txt', 'r') as f:
    for line in f:
        #splitting line w.r.t ',' and storing in x
        x=line.split(',')
        #striping '\n' from last elm of x
        x[-1] = x[-1].strip('\n')
        #adding new row at ith index 
        df.loc[i,:] =x
        i+=1
