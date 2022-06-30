
ss = set([])
s = [70,50,30,100,15,25,20,40]

def SOS(m,n):
    if(m==0):
        return ss
    if(n==0):
        return -1
    
    else:
        if(s[n]>m):
            return (SOS(m,n-1))
        else:
            SOS(m-s[n], n-1)
            ss.add(s[n])
            SOS(m,n-1)


print(SOS(650, len(s)-1))
print(ss)