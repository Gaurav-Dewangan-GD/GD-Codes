
import time

# starttime = time.time()

def gcd(a,b):
    if(b == 0):
        return a
    else:
        return gcd(b,a%b) # % remainder

# print(gcd(192,270))
# print((time.time()-starttime))