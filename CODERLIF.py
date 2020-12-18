#  https://www.codechef.com/problems/CODERLIF


# cook your dish here
t=int(input())
for i in range(t):
    arr=list(int(x) for x in input().split())
    c=0
    l=[]
    c1=0
    s=''
    a=arr.count(0)
    a1=arr.count(1)
    for i in arr:
        s+=str(i)
    if a==0:
        print("#coderlifematters")
    elif a1==0:
        print("#allcodersarefun")
    else:
        a1=s.count("111111")
        if a1>0:
            print("#coderlifematters")
        else:
            print("#allcodersarefun")
        
                
