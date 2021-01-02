class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        arr=''.join(list(map(str,arr)))
        res=''
        for i in range(len(pieces)):
            p=''.join(list(map(str,pieces[i])))
            res+=p
        if len(res)!=len(arr):
            return 0
        for i in range(len(pieces)):
            p=''.join(list(map(str,pieces[i])))
            if p not in arr  :
                return 0
        return 1
