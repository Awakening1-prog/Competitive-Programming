#  https://www.codechef.com/problems/FRK

# cook your dish here
n=int(input())
l=[]
for i in range(n):
    u=input()
    l.append(u)
c=0
for i in l:
    if "ch" in i or "che" in i or "chef" in i  or "hef" in i or "ef" in i or "he" in i : 
        c+=1
print(c)
