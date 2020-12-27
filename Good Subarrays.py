#  https://codeforces.com/problemset/problem/1398/C



from collections import defaultdict
t=int(input())
for i in range(t):
    n=int(input())
    s=input()
    h=defaultdict(int)
    c=0
    ans=0
    for i in s:
        h[c]+=1
        c+=int(i)-1
        ans+=h[c]
    print(ans)
