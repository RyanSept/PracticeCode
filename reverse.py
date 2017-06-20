##def reverse(text):
##    last=text
##    text=list(text)
##    textorig=text
##    text=[]
##    z=0
##    p=''
##    for i in textorig:
##        text.insert(0,textorig[z])
##        z+=1
##    for t in text:
##        p=p+t
##    return p
##        
##        
##def anti_vowel(text):
##    vowel='AaEeIiOoUu'
##    p=''
##    for i in text:
##        if not i in vowel:
##            p=p+i
##    return p
##
##
##def censor(text,word):
##    text=text.split()
##    for i in text:
##        if word==i:
##            text[text.index(i)]='*'*len(word)
##    return ' '.join(text)
            
##        
##def median(seq):
##    seq=list(seq)
##    seq=sorted(seq)
##    mid=len(seq)/2
##    if (mid)*2!=len(seq):
##        return seq[mid]
##    else:
##        return (seq[mid]+seq[mid-1])/2.0
