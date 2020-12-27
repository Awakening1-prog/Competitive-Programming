
#https://www.codechef.com/problems/COOMILK

n=int(input())
for i in range(n):
    n=int(input())
    s=list(input().split())
    a=s.count("cookie")
    a1=s.count("milk")
    if len(s)==1:
        if s[0]=="cookie":
            print("NO")
        else:
            print("YES")
    elif len(s)==2:
        if (s[0]=="cookie" and s[1]=="cookie")or (s[0]=="milk" and s[1]=="cookie"):
            print("NO")
        else:
            print("YES")
    elif s[-1]=="cookie":
        print("NO")
    else:
        for i in range(1,len(s)):
            if (s[i-1]=="cookie" and s[i]=="cookie"):
                print("NO")
                break
        else:
            print("YES")
