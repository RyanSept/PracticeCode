#a is a power of b if b%a==0 and a/b is a power of b
def is_pow(a,b):
    if a==1 or a==0 or a==b:
        return True
    if b%a==0:
        return is_pow(a/b,b)
    else:
        return False

#One way to find the GCD of two numbers is based on the observation that if r is the remainder when a is divided by b, then gcd(a, b) = gcd(b, r). As a base case, we can use gcd(a, 0) = a.
def gcd(a,b):
    if a==0:
        return b
    elif b==0:
        return a
    div=gcd(b,a%b)
    return div

def rot13(s):
    ns=''
    for i in s:
        news=chr(ord(i)+13)
        ns+=news
    print ns
#!usr/bin/python
import rockpaperscissors

def ex2(ps,rs,f1,f2):
    with open(f1,'r') as myf,open(f2,'a+') as myf2:
        for line in myf:
            if line in myf2:
                line=line.replace(ps,rs)
                myf2.write(line)
        myf2.seek(0)    
        print myf2.read() 
ex2('foobar','Lord Frieza','output.txt','memo.txt')

        
        
