#https://www.codechef.com/problems/CNDLOVE/
# cook your dish here
t=int(input())
for i in range(t):
    n=int(input())
    arr=list(int(x) for x in input().split())
    a=sum(arr)
    b=a//2
    b1=a-b
    if b>b1 or abs(b-b1)==1:
        print("YES")
    else:
        print("NO")
