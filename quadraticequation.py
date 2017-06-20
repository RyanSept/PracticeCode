import math
a=raw_input('a:')
b=raw_input('b:')
c=raw_input('c:')
if a>0 and b>0 and c>=0:
    r=(-b+math.sqrt(b**2-4*a*c))/(2*a)
    print r
    j=(-b-math.sqrt(b**2-4*a*c))/(2*a)
    print j
