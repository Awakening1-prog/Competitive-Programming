#  https://codeforces.com/problemset/problem/1409/A




t=int(input())
for i in range(t):
    n,m=map(int,input().split())
    a=abs(n-m)
    if a%10==0:
        print(a//10)
    else:
        print(a//10+1)
