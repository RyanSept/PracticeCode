##def mincoin(coins,s,i):
##    if s==0:
##        return 0
##    if s==[coin for coin in coins]:
##        return 1
##    for i in range(1,s+1):
##        ans+=mincoin(coins,i,i)
##    print ans
##coins=[1,3,5]           
##mincoin(coins,2,len(coins)-1)                
##
##s-coins[i]

##def coop(c,r,i,Ac):
##    if i==0:
##        if c[i]<=Ac: return r[i]
##        else: return 0
##    without_i=coop(c,r,i-1, Ac) 
##    if c[i]>Ac: return without_i 
##    else: with_i=r[i]+coop(c,r,i-1,Ac-c[i]) 
##    return max(with_i, without_i)
##
##c=[1,2,2,3,4,1]
##r=[5,6,8,9,12,4]
##i=len(c)-1
##print coop(c,r,i,5),

##def goddiv(x):
##    for i in range(1,x+1):
##        if x%i==0 and i%2!=0:
##            z=i
##    return z
##def oddiv(x):
##    count=0
##    for i in range(1,x+1):
##        count+=goddiv(i)
##    print count
##oddiv(33)

def drawsq():
    print '+','-'*4,'+'
    print '|',' '*4,'|'
    print '|',' '*4,'|'
    print '+','-'*4,'+',
    
