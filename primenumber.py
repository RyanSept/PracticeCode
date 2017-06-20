##x=13
##k=range(2,x)
##for i in k:
##    x/i
##    if (x%i)==0:
##        print x, "is not a prime number"
##    else: print x, "is not a prime number"
##    break

import time   
def is_prime(x):
    if x>0:
        if x==0 or x==1:
            return False
        if x==2:
            return True
        k=range(2,x)
        n=0
        rem=[]
        for i in range(2,x):
             rem.append(x%i)
        if min(rem)==0:
            return False
        else:return True
    else:
        return False
def isprime(x):
    if x==2: return True 
    for n in range(2,x):
        if x==2 or x==3 or x==5 or x==7:
            return True 
        if x%2==0 or x%3==0 or x%5==0 or x%7==0:
            return False 
        elif (x%n)==0 :
            return False
        else:return True
start_time = time.time()        
for i in range(1000):
    print isprime(i),i
print("--- %s seconds ---" % (time.time() - start_time))
