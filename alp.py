#  https://www.codechef.com/problems/ALPHABET


# cook your dish here
s=input()
c=0
n=int(input())
for i in range(n):
    s1=input()
    for i in s1:
        if i  not in s:
           print("No")
           break
    else:
        print("Yes")
