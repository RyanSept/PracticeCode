#-*-coding:utf8;-*-

import time

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
pfs=[] 
ans=[]
def func() :
    n=1
    for i in pfs:
        if type(i)==list:
            ans.append(min(i))
    ans.append(pfs[-1])
    for i in ans:
        n*=i
    print "The prime factors of "+str(n)," are:",ans

def pfactor(x):
    l=[]
    if x==0 or x==1:
        return None
    if isprime(x) :
        pfs.append(x) 
    else:
        for n in range(2,x):
            if isprime(n) and x%n==0:
                l.append(n)
        pfs.append(l)
        pfactor(x/min(l))

start_time = time.time()
for i in range(2,1000):
    pfactor(i)
    func()
    pfs=[]
    ans=[]
print("--- %s seconds ---" % (time.time() - start_time))
print ans

            
####TIME COMPARISONS####
##from math import sqrt
##def prime_factors(n):
##    num = []
##
##    #add 2 to list or prime factors and remove all even numbers(like sieve of ertosthenes)
##    while(n%2 == 0):
##        num.append(2)
##        n /= 2
##
##    #divide by odd numbers and remove all of their multiples increment by 2 if no perfectlly devides add it
##    for i in xrange(3, int(sqrt(n))+1, 2):
##        while (n%i == 0):
##            num.append(i)
##            n /= i
##
##    #if no is > 2 i.e no is a prime number that is only divisible by itself add it
##    if n>2:
##        num.append(n)
##
##    print (num)
##
##def primes(n):
##    primfac = []
##    d = 2
##    while d*d <= n:
##        while (n % d) == 0:
##            primfac.append(d)  # supposing you want multiple factors repeated
##            n //= d
##        d += 1
##    if n > 1:
##       primfac.append(n)
##    print primfac
##
##start_time = time.time()                
##for i in range(2,1000):
##    primes(i)
##print("--- %s seconds ---" % (time.time() - start_time))
