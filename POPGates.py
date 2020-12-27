


# cook your dish here
t=int(input())
for i in range(t):
    n,k=map(int,input().split())
    arr=list(input().split())
    s=arr[-1]
    for j in range(k):
        if arr[-1]=="H":
           arr.pop(len(arr)-1)
           for i in range(len(arr)):
               if arr[i]=="H":
                   arr[i]="T"
               else:
                   arr[i]="H"
        elif arr[-1]=="T":
           arr.pop(len(arr)-1)
    #print(arr)
    print(arr.count("H"))
