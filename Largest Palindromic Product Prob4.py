def palindrome(x):
    x=str(x)
    if x==x[::-1]:
        return True
ans=[]
for i in range(100,1000):
    for k in range(100,1000):
        z=i*k
        if palindrome(z):
            ans.append(z)

print max(ans)
