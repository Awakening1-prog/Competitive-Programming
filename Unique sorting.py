https://www.hackerearth.com/practice/algorithms/greedy/basics-of-greedy-algorithms/practice-problems/algorithm/unique-sorting-17d60d9f/description/


t=int(input())
for i in range(t):
    s=input()
    a="0123456789"
    res=''
    for i in s:
        if i in a:
            res+=i
    i=0
    s=list(s)
    while i<len(s):
        if s[i] in a:
            s.remove(s[i])
        else:
            i+=1
    res1=''
    for i in range(len(res)):
        if int(res[i])%2!=0:
            res1+=res[i]
    res1=sorted(res1)

    for i in range(len(res)):
        if int(res[i])%2==0:
            res1+=res[i]
    res2=''
    for i in range(len(s)):
        if (ord(s[i])-ord("a"))%2!=0:
            res2+=s[i]
    res2=sorted(res2)
    for i in range(len(s)):
        if (ord(s[i])-ord("a"))%2==0:
            res2+=s[i]
    print(''.join(res2)+''.join(res1))
