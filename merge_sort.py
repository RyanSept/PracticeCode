def merge(a,b):
    """ Function to merge two arrays """
    c = []
    print a
    while len(a) != 0 and len(b) != 0:
        if a[0] < b[0]:
            c.append(a[0])
            a.remove(a[0])
        else:
            c.append(b[0])
            b.remove(b[0])
    if len(a) == 0:
        c += b
    else:
        c += a
    return c

# Code for merge sort
call=0
def mergesort(x):
    global call
    call+=1
    
    """ Function to sort an array using merge sort algorithm """
    if len(x) == 0 or len(x) == 1:
        return x
    else:
        middle = len(x)/2
        
        a = mergesort(x[:middle])
        b = mergesort(x[middle:])
    res = merge(a,b)
    return res

l=[21, 1, 26, 45, 29, 28, 2, 9, 16, 49, 39, 27, 43, 34, 46, 40]
print mergesort(l)
print call
