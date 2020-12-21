#  https://codeforces.com/problemset/problem/1397/A




t=int(input())
for i in range(t):
    n=int(input())
    h={}
    for i in range(n):
        s=input()
        for i in s:
            if i not in h:
                h[i]=1
            else:
                h[i]+=1
    for key,val in h.items():
        if val%n!=0:
            print("NO")
            break
    else:
        print("YES")
