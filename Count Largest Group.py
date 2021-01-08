class Solution:
    def countLargestGroup(self, n: int) -> int:
        if n<10:
            return n
        else:
            h=defaultdict(list)
            for i in range(1,n+1):
                x=sum(list(map(int,str(i))))
                h[x].append(i)
            print(h)
            l=[]
            for key,val in h.items():
                l.append(len(val))
            l.sort()
            l=l[::-1]
            print(l)
            return l.count(l[0])
