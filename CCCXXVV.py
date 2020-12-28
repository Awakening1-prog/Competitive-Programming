class Solution:
    def solve(self, numeral):
        h={
        'M': 1000,
        'D': 500,
        'C': 100,
        'L': 50,
        'X': 10,
        'V': 5,
        'I': 1
        }
        print(h)
        res=0
        for i in range(len(numeral)):
            if i>0  and h[numeral[i]]>h[numeral[i-1]]:
                res+=h[numeral[i]]-2*h[numeral[i-1]]
            else:
                res+=h[numeral[i]]
            print(res)
        return res
