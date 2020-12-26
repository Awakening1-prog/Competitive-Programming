from collections import defaultdict
import operator
def solve(nums):
    h=defaultdict(list)
    for i in nums:
        h[nums.count(i)].append(i)
    p=dict(sorted(h.items(),key=operator.itemgetter(0),reverse=True))
    l=[]
    for key,val in p.items():
        val.sort()
        l+=val
    print(*l)
t=int(input())
for i in range(t):
    n=int(input())
    arr=list(int(x) for x in input().split())
    solve(arr)
