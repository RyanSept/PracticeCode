##def pad(x):
##    k=range(1,x)
##    list1=[]
##    abund=[]
##    list2=[]
##    for v in k:
##        if x%v==0:
##            list1.append(v)
##    if sum(list1)==x:
##        print x, "is a perfect number"
##    elif sum(list1)>x:
##        abund.append(x)
##        print abund
##        print x, "is an abundant number"
##    else:
##        print x, "is a deficient number"

def isab(x):
    k=range(1,x)
    divisors=[]
    abund=[]
    list2=[]
    for v in k:
        if x%v==0:
            divisors.append(v)
    if sum(divisors)>x:
        return True
    else:
        return False
        
z=1
zeus=[]
ares=[]
while z<28123:
    z=z+1
    isab(z)
    if isab(z)==True:
        zeus.append(z)

for i in zeus:
    print i+i
    
