##n=6
##if n>0 and (n/2)*2==n:
##    n=n/2
##    if n>1 and (n/2)*2!=n:
##        n=(n*3)+1
##    else:
##        n=(n*3)+1
##    print n
##
n=100000000000
list1=[]
while n>1:
    if n>0 and (n/2)*2==n:
        n=n/2
        print n
    else:
        n=(n*3)+1
        print n
    list1.append(n)
print 'The cycle length of the value is', len(list1)+1

