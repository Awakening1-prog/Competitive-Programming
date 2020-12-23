#   https://codeforces.com/problemset/problem/1406/A



t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    a.sort()
    res1=0
    res2=0
    for i in a:
        if i==res1:
            res1+=1
        elif i==res2:
            res2+=1
    print(res1+res2)
