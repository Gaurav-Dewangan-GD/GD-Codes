from gcdusingeuclids import *

def lcm(a,b):
    return(int((a*b)/gcd(a,b)))

def count_problem(a,b):
    l = reduce(lcm,a)
    g = reduce(gcd,b)
    
    count = 0
    for i in range(l,g+1):
        if g%i == 0:
            count +=1    
    return count


