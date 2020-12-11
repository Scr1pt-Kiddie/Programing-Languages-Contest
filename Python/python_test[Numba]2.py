import math
from time import perf_counter
from numba import njit, prange, vectorize, int32, int64
import numba as nb
import numpy as np

@vectorize([int64(int64,int64)])
def is_prime(num, divs):
    if num == 2:
        return True
    if num <= 1 or not num % 2:
        return False
    
    if not num % divs:
        if divs == num :
            return True
        return False
    return True

@njit(fastmath=True, parallel=True, cache=True)
def run_program(N):
    num= np.arange(N)
    divs = np.arange(3, int(math.sqrt(N)) + 1, 2)
    for i in prange(N):
        
        ans = is_prime(num[i],divs)


if __name__ == '__main__':
    N = 10000000
    start = perf_counter()
    run_program(N)
    end = perf_counter()
    print(end - start)
