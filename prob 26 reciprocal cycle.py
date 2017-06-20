i=6
i=float(i)
list1=[]
ans=1/i
ans=str(ans)
if len(ans)<12:
    print ans,"is not recurring"
else:
    ans=ans[2:]
    zeus=[]
    list1.append(ans)
    print list1

    for x in ans:
        if x==x:
            zeus.append(x)
    print zeus
    
    print ans[2]
