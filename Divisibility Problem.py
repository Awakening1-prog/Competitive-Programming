#  https://codeforces.com/problemset/problem/1328/A



t=int(input())
for _ in range(t):
    n,m=map(int,input().split())
    if n%m==0:
        print(0)
    else:
        res=n%m
        print(m-res)
