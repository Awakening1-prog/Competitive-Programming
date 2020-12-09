 # https://www.codechef.com/problems/ZCOPREP
 # cook your dish here
for i in range(int(input())):
    n,m,s=list(int(x) for x in input().split())
    arr=list(int(x) for x in input().split())
    arr.sort()
    c=0
    for i in range(n):
        if m==0:
           break
        if arr[i]<=s:
            c+=1
            m=m-1
        else:
            if arr[i]<=2*s and m>=2:
               c+=1
               m=m-2
            else:
                break
    print(c)