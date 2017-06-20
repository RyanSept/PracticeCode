#-*-coding:utf8;-*-
#qpy:2
#qpy:console

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

res=[]
def cprime(n):
    if (n/2)*2==n:
        pass
    if isprime(n):
        l=list(str(n))
        ans=[] 
        for i in range(len(l)):
            l.append(l.pop(0))
            s=''
            for z in l:
                s+=z
                if isprime(int(s)) and len(s)==len(l) :
                    ans.append(1)
                else:
                    if len(s)==len(l):
                        ans.append(0)
        if 0 in ans:
            pass
        else:
            res.append(1)
    else:
        pass
      
for i in range(10000,12000):
    cprime(i)
print len(res)
