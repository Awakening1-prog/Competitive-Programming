t=int(input())
for i in range(t):
    n=int(input())
    arr=list(int(x) for x in input().split())
    #h={}
    c=0
    for i in range(len(arr)):
        h={}
        for j in range(i,len(arr)):
            if arr[j] not in h:
                h[arr[j]]=1
                c+=len(h)
            else:
                break
    print(c)
