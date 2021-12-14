import math
#we need 2 functions. The "outer" function will count how many cookies I get initially for my many and calls the calls the second, recursive function to calculate the number of cookies I get from the wrappings of the cookies

#the recursive function has just 2 anguments, the number of cookies and for how many wrappers I get back a cookie
def rec(c,w):
    
    if c<w:
        return 0
    cookies = math.floor(c/w)
    #in the recursion the new amount of cookies is the number I get back + the number of cookies I did not used
    return cookies + rec(cookies + c%w,w)

def cookies(m,p,w):
    if not isinstance(w, int):
        print ("inapt input")
        quit()
    c = math.floor(m/p)
    return c + rec(c,w)