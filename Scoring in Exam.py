# https://www.hackerearth.com/practice/algorithms/sorting/merge-sort/practice-problems/algorithm/scoring-in-exam-1/description/




# Write your code here
n,k=map(int,input().split())
t=list(int(x) for x in input().split())
s=list(int(x) for x in input().split())
s.sort()
t.sort()
for i in range(k):
    q=int(input())
    print(sum(t[-q:]))
