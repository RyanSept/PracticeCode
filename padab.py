def is_int(x):
    if x>0:
        if x-x//1>0:
            return False
        else:
            return True
    else:
        if x%1==0.0:
            return True
        if x-((x//1)+1)<0:
            return False
        else:
            return True
