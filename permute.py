def permute(lst):
    originallst=tuple(lst)
    l=[]
    x=0
    while list(originallst) not in l:
        lst.insert(x,lst[-1])
        lst.pop(-1)
        l.append(lst)
        x+=1
        print l
    print l
permute([1,2,3])
