##for i in range(1,x):
##    x=x*i
##print x
def factorial(n):
    if n==0:
        return 1
    else:
        x=factorial(n-1)
        ans=n*x
        print ans
        return ans

x=raw_input("Insert a value: ")
factorial(int(x))
