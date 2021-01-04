class Solution:
    def solve(self, s):
        h=defaultdict(int)
        if len(s)<=1:
            return False
        res=''
        for i in range(len(s)//2):
            res+=s[i]
            if res*(len(s)//len(res))==s:
                return True
        return False
