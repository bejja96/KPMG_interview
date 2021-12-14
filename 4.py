import numpy as np

def euc_norm(array):
    return np.sqrt(np.sum(np.square(array),axis=1))