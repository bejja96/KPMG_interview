def towers(list):
    
    #first of all I check if the inputs are suitable for the game
    for i in range(len(list)):
            if not isinstance(list[i], int):
                print ("inapt input")
                quit()

    l = len(list)
    surf = 0
    if l == 0:
        print("no towers :(")   
    else:
        #at this point I had 2 options to handle the first tower, which does not have a neighbour from the left
        #1. (what I did) count teh area independent from the others
        #2. put another condition in the foor loop to check if "i" is the first or not

        #to calculate the surface of the towers there are two main things:
        #1. the surface of the cubes in a tower that is attached - we have to subtract height of the tower -1 twice
        surf = list[0]*6 - max(0,2*(list[0]-1))
        for i in range(1,l):
            surf = surf + list[i]*6 - max(0,2*(list[i]-1))
            #2. the attached surface of the the towers - we have to subtract the height of the smaller tower twice
            surf = surf - min(2*list[i],2*list[i-1])
    return surf

l1 = [0,1,3,1]
print(towers(l1))