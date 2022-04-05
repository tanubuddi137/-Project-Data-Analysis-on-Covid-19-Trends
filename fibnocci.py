
def fibnoci(a):
    if a == 0:
        return 0
    elif a == 1:
        return 1
    else:
        return fibnoci(a-1) + fibnoci(a-2)
        
