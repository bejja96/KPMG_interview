def chess(n: int, rq: int, cq: int, k):

    #first of all I check if the inputs are suitable for the game
    if not isinstance(n, int) or not isinstance(rq, int) or not isinstance(cq, int):
        print ("inapt input")
        quit()
    if 0 > rq > n or 0 > cq > n or len(k[0]) != 2:
        print ("inapt input")
        quit()
    for i in range(len(k)):
        for j in range(len(k[0])):
            if 0 < k[i][j] <= n and isinstance(k[i][j], int):
                continue
            else:
                print ("inapt input")
                quit()
    num_sq = 0
#I am sure, there are mutiple variations of solutions and I know, that mine is a bit brute force but it works
#I simply used 8 while loops for the 8 movement directions
#rp an cp are the current row and column positions that I have to check
    rp = rq + 1
    cp = cq + 1
    while 0 < rp <= n and 0 < cp <= n:
        #if I find an obstacle, that route is closed and I can skip to the other directions
        for i in range(len(k)):
            if rp == k[i][0] and cp == k[i][1]:
                #this is for getting out of the while loop
                rp = -1
                #this is a little correction, because, when we get out of the loop, it will still add 1 to the number of squares
                num_sq = num_sq - 1
                break
        num_sq = num_sq + 1
        rp = rp + 1
        cp = cp + 1
#----------------------------------------
    rp = rq + 1
    cp = cq
    while 0 < rp <= n and 0 < cp <= n:
        for i in range(len(k)):
            if rp == k[i][0] and cp == k[i][1]:
                rp = -1
                num_sq = num_sq - 1
                break
        num_sq = num_sq + 1
        rp = rp + 1
#----------------------------------------
    rp = rq
    cp = cq + 1
    while 0 < rp <= n and 0 < cp <= n:
        for i in range(len(k)):
            if rp == k[i][0] and cp == k[i][1]:
                rp = -1
                num_sq = num_sq - 1
                break
        num_sq = num_sq + 1
        cp = cp + 1
#----------------------------------------
    rp = rq + 1
    cp = cq - 1
    while 0 < rp <= n and 0 < cp <= n:
        for i in range(len(k)):
            if rp == k[i][0] and cp == k[i][1]:
                rp = -1
                num_sq = num_sq - 1
                break
        num_sq = num_sq + 1
        rp = rp + 1
        cp = cp - 1
#----------------------------------------
    rp = rq - 1
    cp = cq + 1
    while 0 < rp <= n and 0 < cp <= n:
        for i in range(len(k)):
            if rp == k[i][0] and cp == k[i][1]:
                rp = -1
                num_sq = num_sq - 1
                break
        num_sq = num_sq + 1
        rp = rp - 1
        cp = cp + 1
#----------------------------------------
    rp = rq - 1
    cp = cq - 1
    while 0 < rp <= n and 0 < cp <= n:
        for i in range(len(k)):
            if rp == k[i][0] and cp == k[i][1]:
                rp = -1
                num_sq = num_sq - 1
                break
        num_sq = num_sq + 1
        rp = rp - 1
        cp = cp - 1
#----------------------------------------
    rp = rq - 1
    cp = cq
    while 0 < rp <= n and 0 < cp <= n:
        for i in range(len(k)):
            if rp == k[i][0] and cp == k[i][1]:
                rp = -1
                num_sq = num_sq - 1
                break
        num_sq = num_sq + 1
        rp = rp - 1
#----------------------------------------
    rp = rq
    cp = cq - 1
    while 0 < rp <= n and 0 < cp <= n:
        for i in range(len(k)):
            if rp == k[i][0] and cp == k[i][1]:
                rp = -1
                num_sq = num_sq - 1
                break
        num_sq = num_sq + 1
        cp = cp - 1
    return num_sq


k =[[3,3],[4,5]]
y = chess(6,1,3,k)
print(y)