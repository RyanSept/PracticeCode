import math
def eqtofac(x):
    y=str(x)
    count=0
    for i in y:
        z=math.factorial(int(i))
        count+=z
    if count==x and count!=1 and count!=2:
        print count
ans=0
for i in range(50000):
    ans+=eqtofac(i)


