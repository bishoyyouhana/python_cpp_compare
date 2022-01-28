import numpy as np
import time
def runtime():
    k_max = 40000
    N = 10000

    data = np.zeros((2,N))
    coefs = np.zeros((k_max,2),dtype=float)

    t1 = time.time()
    for k in range(1,k_max+1):
        cos_k = np.cos(k*data[0,:])
        sin_k = np.sin(k*data[0,:])
        coefs[k-1,0] = (data[1,-1]-data[1,0]) + np.sum(data[1,:-1]*(cos_k[:-1] - cos_k[1:]))
        coefs[k-1,1] = np.sum(data[1,:-1]*(sin_k[:-1] - sin_k[1:]))
    t2 = time.time()

    return t2-t1