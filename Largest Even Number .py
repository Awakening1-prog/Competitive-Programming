def maxSumWithK( a, n, k):
    
    res=0
    m=-10000000
    for i in range(k):
        res+=a[i]
    m=max(m,res)
    for i in range(k,n):
        j=0
        while i-j>=k:
            res+=a[i]-a[j]
            j+=1
        m=max(m,res)
    m=max(m,res)
    return m
            
