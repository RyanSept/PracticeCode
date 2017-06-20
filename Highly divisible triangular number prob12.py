def nthTriangleNo(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    r=nthTriangleNo(n-1)
    ans=n+r
    return ans

def countdiv(x):
    count=0
    for i in range(1,x+1):
        if x%i==0:
            count+=1
    return count

##x=500
##while True:
##    try:
##        if countdiv(nthTriangleNo(x))==500:
##            print x
##    except Exception as e:
##        print str(e)
##        print x
##        break
##    x+=1
    

