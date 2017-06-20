def palindrome(x):
    x=str(x)
    revx=x[::-1]
    if x==revx:
        return True
    else:
        return False
lst=[]
for i in range(1,1000000):
    if palindrome(bin(i)[2:]) and palindrome(i):
        print i
        lst.append(i)
print sum(lst)
        
        
        
    
