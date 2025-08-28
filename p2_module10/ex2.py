import os
import time
from multiprocessing import Pool

def square(x):
    print(f'{os.getpid()} calculating square of  {x}')
    time.sleep(3)
    return x*x
if __name__=="__main__":
    start=time.time()
    with Pool(4) as pool: #cand vrem sa controlam resursele utilizate
        result=pool.map(square,[1,2,3,4,5])
        print(result)
    end=time.time()
    print(end-start)