'''
Here, we break our process into multiple tasks and all of them run independently.
'''
# example of multiprocessing 

# importing required libraries
import pandas as pd
import math
import multiprocessing as mp
from random import randint

# function to calculate the number of divisors
def countDivisors(n) : 
    count = 0
    for i in range(1, (int)(math.sqrt(n)) + 1) : 
        if (n % i == 0) : 
            if (n / i == i) : 
                count = count + 1
            else :  
                count = count + 2
    return count 


# create one million points at random 
random_data = [randint(10,1000) for i in range(1,1000001)]

data = pd.DataFrame({'Number' : random_data })

pool = mp.Pool(processes = (mp.cpu_count() - 1))
answer = pool.map(countDivisors,random_data)
pool.close()
pool.join()
