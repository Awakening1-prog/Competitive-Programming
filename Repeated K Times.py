#https://www.hackerearth.com/practice/algorithms/searching/linear-search/practice-problems/algorithm/repeated-k-times/description/




t=1
for i in range(t):
    n=int(input())
    arr=list(int(x) for x in input().split())
    k=int(input())
    h={}
    l=[]
    for i in arr:
        if i not in h:
            h[i]=1
        else:
            h[i]+=1
    for key,val in h.items():
        if val==k:
            l.append(key)
    print(min(l))
