

#https://www.hackerearth.com/practice/codemonk/


t=int(input())
l=[]
dp=[0]*26
for i in range(t):
    a=input()
    l.append(a)
for i in range(len(l)):
    res=0
    for j in range(i):
        if l[i]>l[j]:
            res+=1
    print(res)
