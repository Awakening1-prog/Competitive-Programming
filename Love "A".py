#  https://codeforces.com/problemset/problem/1146/A


for i in range(1):
    s=input()
    a=s.count("a")
    if a>len(s)//2:
        print(len(s))
    else:
        s=sorted(s)
        #print(s)
        while s.count("a")<=len(s)//2:
            s.pop()
        print(len(s))
