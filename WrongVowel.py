# https://www.codechef.com/problems/MISPRNT

# cook your dish here
t=int(input())
for i in range(t):
    n=int(input())
    l=list(input())
    c=0
    arr=list(input())
    for i in range(len(arr)):
        if arr[i] in l and arr[i].isalpha():
            c+=1
    print(c)
