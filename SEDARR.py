#  https://www.codechef.com/LTIME91B/problems/SEDARR

t=int(input())
for i in range(t):
    a,b=map(int,input().split())
    arr=list(int(x) for x in input().split())
    if sum(arr)%b==0:
        print(0)
    else:
        print(1)
