x=3
y=5
k=range(1,1000)
list1=[]
for i in k:
    ans=x*i
    ans2=y*i
    while ans<1000:
        list1.append(ans)
        break
    while ans2<100:
        list1.append(ans2)
        break
print sum(list1)

