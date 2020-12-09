# https://www.codechef.com/problems/KS2


# cook your dish here
for i in range(int(input())):
    n=input()
    s=sum(map(int,n))
    print(n+str((10-s)%10))