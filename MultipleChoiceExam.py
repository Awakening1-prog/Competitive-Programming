# https://www.codechef.com/problems/EXAM1


# cook your dish here
t=int(input())
for i in range(t):
    n=int(input())
    arr1=input()
    arr2=input()
    c=0
    i=0
    while i<n:
        if arr1[i]==arr2[i] :
            c+=1
        elif arr1[i]!=arr2[i] and arr2[i]=="N":
            c+=0
        elif arr1[i]!=arr2[i]:
            i+=1
        i+=1
    print(c)
