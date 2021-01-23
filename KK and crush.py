# Write your code here
t=int(input())
for i in range(t):
    n=int(input())
    arr=list(int(x) for x in input().split())
    h={}
    for i in arr:
        if  i not in h:
            h[i]=1
    q=int(input())
    for i in range(q):
        a=int(input())
        if a in h:
            print("Yes")
        else:
            print("No")
        
