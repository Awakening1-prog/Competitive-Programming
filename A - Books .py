# https://www.codechef.com/problems/BIT2A


# cook your dish here
t=int(input())
for i in range(t):
    n=int(input())
    arr=list(int(x) for x in input().split())
    l=[]
    for i in range(n):
        c=0
        for j in range(i+1,n):
            if arr[i]<arr[j]:
                c+=1
        l.append(c)
    print(*l)
