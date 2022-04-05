

def merge(a,b):
    c = []
    i = 0
    j = 0
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1
    if i < len(a):
        c.extend(a[i:])
    if j < len(b):
        c.extend(b[j:])
    return c

a=[1,3,5,7,9]
b=[2,4,6,8,10]
c= merge(a,b)
print(c)

