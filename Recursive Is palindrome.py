def first(word):
    return word[0]

def last(word):
    return word[-1]

def middle(word):
    return word[1:-1]

def recpalindrome(s):
    if len(s)<=1:
        return True
    f=first(s)
    m=middle(s)
    l=last(s)
    if f==l:
        return recpalindrome(m)
    else:
        return False
print recpalindrome('otton')
