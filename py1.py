##x=16
##ans=0
##while ans*ans<x: 
##      ans = ans + 1 
##print ans

##sumDigits = 0 
##for c in str(1952): 
##    sumDigits += int(c) 
##print sumDigits 

##x = 100 
##divisors = [] 
##for i in range(1,x): 
##    if x%i == 0: 
##     divisors=divisors+[i] 
##n = 10
##while n > 0:
##    print n
##    n = n-1
##print 'Blastoff!'
##n = 10
##while True:
##    print n, 
##    n = n - 1
##print 'Done!'
##while True:
##    line = raw_input('> ')
##    if line == 'done':
##        break
##    print line
##print 'Done!'

##line=raw_input('>')
##sumDigits=0
##for x in '123':
##	sumDigits = sumDigits+int(x)
##print sumDigits
##for x in [1,2,3]:
##print x






##def digit_sum(n):
##  sumDigits = 0 
##  for c in str(n): 
##      sumDigits += int(c) 
##  print sumDigits 
##def sqrt(x): 
##  """Returns the square root of x, if x is a perfect square. 
##       Prints an error message and returns None otherwise""" 
##  ans = 0 
##  if x >= 0: 
##      while ans*ans < x: ans = ans + 1 
##      if ans*ans != x: 
##          print x, 'is not a perfect square' 
##          return None 
##      else: return ans 
##  else: 
##        print x, 'is a negative number' 
##        return None 
##
