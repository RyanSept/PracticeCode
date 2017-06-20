##def cuberoot(x):
## answer=0
## if x>0:
##    while answer*answer*answer<=x:
##        answer=answer+1
##    if answer*answer*answer!= x:
##     print "no cuberoot"
##    else: print answer
## else:
##  if x<0:
##     while answer*answer*answer>=x:
##         answer=answer-1
##     if answer*answer*answer != x:
##      print x, "is not a perfect cube"
##      return None
##     else: print answer, "is the cuberoot"


def croot(x):
    "Returns cube root of x if x is perfect cube"
    y=0
    if x>=0:
        while y**3<x:
            y=y+1
        if y**3==x: print y
        else: print "not perfect cube"
    else:
        if x<=0:
            while y**3>x: y=y-1
        if y**3==x: print y
        else: print "not perfect cube"
