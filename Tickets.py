# https://www.codechef.com/problems/TICKETS5


# cook your dish here
t=int(input())
for i in range(t):
    s=input()
    def m(s):
        s=list(s)
        if len(s)==0 and len(s)==1:
            return 0
        k=set(s)
        if len(k)>2:
            return 0
        if s[0]!=s[1]:
            return 1
        else:
            return 0
        for i in range(0,len(s)-2):
            if s[i]==s[i+2] :
                return 1
            else:
                 return 0
        for i in range(1,n-2,2):
            if s[i]==s[i+1]:
                return 1
            else:
                return 0
    if (m(s)):
        print("YES")
    else:
        print("NO")
