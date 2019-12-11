import os
os.chdir(r"D:\DS_challenges\CS4003 DA Projects\CS4003 Projects\Data Set")
i=0
with open(r'CANCER.txt', 'r') as f:
    for line in f:
        x=line.split(',')
        x[-1] = x[-1].strip('\n')
        df.loc[i,:] =x
        i+=1
