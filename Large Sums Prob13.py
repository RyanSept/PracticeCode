count=0
from datetime import datetime
with open('peuler13.txt','r') as myf:
    start=datetime.now()
    for line in myf:
        count+=int(line)
    ans=str(count)
    print ans[:10]
    end=datetime.now()-start
    print end



        
    
