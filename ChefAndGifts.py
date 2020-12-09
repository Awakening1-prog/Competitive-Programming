# https://www.codechef.com/problems/PRGIFT

# cook your dish here
for i in range(int(input())):
    n,k=list(int(x) for x in input().split())
    arr=list(int(x) for x in input().split())
    c=0
    c1=0
    if k==0:
        for i in range(n):
            if arr[i]%2==0:
                c1=c1+1
        if c1==n:
            print("NO")
        else:
            print("YES")
    else:
    
        for i in range(n):
           if arr[i]%2==0:
               c+=1
        if k<=c:
           print("YES")
        else:
           print("NO")
