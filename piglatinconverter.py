w=raw_input("Enter a word in English:") 
if len(w)>0 and w.isalpha():
        pyg='ay'
        first= w[0]
        second=w[1]
        last= w[-1]
        w= w[2:-1]
        w= w+last+first+second+pyg
        print w
else:
    print "Not a word"

    
