##matrix=[['0','1','1','0','0'],['0','1','1','1','0'],['0','1','0','1','0']]
##def print_matrix(matrix):
##    for row in matrix:
##        print " ".join(row)
##        
##subm=[]
##def subarr(matrix):
##    for r in matrix:
##        r=
##    if matrix[r][c]=='1':
##        if matrix[r][c]==matrix[r+1][c]:
##            if matrix[r][c]==matrix[r][c+1]:
##                if matrix[r][c]==matrix[r+1][c+1]:
##                    print r,c
##                    print matrix[r][c],matrix[r][c+1]
##                    print matrix[r+1][c], matrix[r+1][c+1]
##    else:
##        r=r+1
##        c=c+1
##        subarr(matrix)
###print_matrix(matrix)

def max_subarray(A):
    max_ending_here = max_so_far = 0
    for x in A:
        max_ending_here = max(0, max_ending_here + x)
        print max_ending_here
        max_so_far = max(max_so_far, max_ending_here)
        print max_so_far
    return max_so_far

##def max_subarray2(lst,i,val):
##    if len(lst)==0:
##        return 0
##    val=0
##    if lst[i]>0:
##        if i>0:
##            val+=lst[i]
##            take=max_subarray2(lst,i-1,val+lst[i])
##    print max(val)
    
    
val=0
lst=[5,4,2]
i=len(lst)-1            
max_subarray2(lst,i,val)
        

    

    
    
    
    
