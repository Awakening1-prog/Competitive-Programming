class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        c=0
        h=defaultdict(int)
        for i in range(len(deliciousness)):
            x=1
            for j in range(0,22):
                x1=x-deliciousness[i]
                if h[x1]:
                    c+=h[x1]
                    c=c%(1_000_000_007)
                x=x*2
            h[deliciousness[i]]+=1

        #print(h)
        return c%(1_000_000_007)
