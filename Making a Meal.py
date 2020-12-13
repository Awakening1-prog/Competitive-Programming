#  https://www.codechef.com/problems/CFMM



t=int(input())
for j in range(t):
    n=int(input())
    s=''
    for i in range(n):
        a=input()
        s+=a
    c=s.count("c")
    o=s.count("o")
    d=s.count("d")
    e=s.count("e")
    h=s.count("h")
    f=s.count("f")
    print(min(c//2,o,d,e//2,h,f))
