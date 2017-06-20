import random
import time
x=[]
while len(x)<12:
    x.append(random.randrange(1,120))
    x.sort()
def bsearch(q,lst):
    start=time.clock()
    mid=len(lst)/2
    if lst[mid]==q:
        print "Hurrah we found it",lst[mid]
    elif len(lst)<2 and not q in lst:
        print q,'is not in the list'
    else:
        if lst[mid]>q:
            left=lst[0:mid]
            print left
            bsearch(q,left)
        else:
            right=lst[mid:]
            print right
            bsearch(q,right)
    end=time.clock()-start
    print end
    end=0


