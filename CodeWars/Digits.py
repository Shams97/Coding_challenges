def findDigit(n,p):
    n = str(n)
    sig = 0
    for i in range(len(n)):
        sig += pow(int(n[i]),p)
        p += 1
    k = sig / int(n) 
    if(k == int(k)):
        return int(k)
    return -1
    

#Solved
