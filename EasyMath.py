# https://www.codechef.com/problems/RPD

t=int(input())
for i in range(t):
    n=int(input())
    l=[]
    k=[]
    arr=list(int(x) for x in input().split())
    def m(n):
        if len(str(n))==1:
            return n
        return n%10+m(n//10)
        
    for i in range(n):
        for j in range(i+1,n):
            l.append(arr[i]*arr[j])
    for i in range(len(l)):
        a=m(l[i])
        k.append(a)
    print(max(k))
