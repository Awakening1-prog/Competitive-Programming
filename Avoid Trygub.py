#   https://codeforces.com/problemset/problem/1450/A


from collections import Counter
t=int(input())
for i in range(t):
    n=int(input())
    s=input()
    s1="trygub"
    h={}
    for i in s:
        if i not in h:
            h[i]=1
        else:
            h[i]+=1
    if "t" in h:
        s=s.replace('t','')
        s=s+"t"*h["t"]
        print(s)
    else:
        print(s)
