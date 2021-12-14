import numpy as np

def chessboard(n: int):

    if 0 < n and not isinstance(n, int):
        print ("inapt input")
        quit()
        
    chessb = np.ones((n,n))

    for i in range(n):
        for j in range(n):
            if (i+j)%2 != 0:
                chessb[i][j] = -1
    return chessb