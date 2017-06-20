##def evenodd(x):
##    "Indicates if x is odd or even"
##    if x>0 and (x/2)*2==x:
##        print x, "is even"
##    else:
##        print x, "is odd"
##        
##n=2589
##n=str(n)
##for i in n:
##    if n.index(i)<len(n):
##        x=n[n.index(i)+1]
##        ans=int(i)+int(x)
##        ans=ans+int(n[-1])
##print ans 
##
##numCalls=0
##def fib(n):
##    global numCalls 
##    numCalls += 1
##    print 'fib called with', n
##    if n <= 1: return 1
##    else: return fib(n-1) + fib(n-2)
##    print numCalls,"on",n

def factorial(n):
	if n == 0: return 1
	return n*factorial(n-1)
