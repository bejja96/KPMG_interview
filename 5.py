import numpy as np

def matrix(list):
    #rest_size will the size of the space that is to fill with zeros (how big is matrix before I add the next one)
    rest_size = len(list)
    matrix = list[0]
    for i in range(1,len(list)):
        act_size = len(list[i])
        #for every block I have to add, I generate a block of zeros that fills the needed space
        mz = np.zeros([rest_size,act_size])
        matrix=np.hstack((matrix,mz))

        #in case of 1element matrix
        x = np.atleast_2d(list[i])
        
        #here I use the same block of zeros just transposed, because of the shape of the space, merge it with the recent matrix and add it to the big matrix
        a = np.hstack((np.transpose(mz),x))
        matrix = np.vstack([matrix,a])

        rest_size = rest_size + act_size
    print(np.matrix(matrix))

A = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
B = [[10, 11],[12, 13]]
C = [14]


K = [A,B,C ]
matrix(K)