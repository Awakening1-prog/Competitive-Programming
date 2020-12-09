#https://www.codechef.com/problems/CEQUAL
# cook your dish here
for i in range(int(input())):
    n=int(input())
    arr=list(int(x) for x in input().split())
    l=set(arr)
    if n==len(l):
        print("No")
    else:
        print("Yes")