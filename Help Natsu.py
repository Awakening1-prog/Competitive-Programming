#  https://www.hackerearth.com/practice/algorithms/sorting/merge-sort/practice-problems/algorithm/help-natsu/description/




'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''
from collections import defaultdict
# Write your code here
t=int(input())
for i in range(t):
    h={}
    n=int(input())
    for i in range(n):
        s=input()
        if s not in h:
            h[s]=1
        else:
            h[s]+=1
    h1=defaultdict(list)
    for key,val in h.items():
        h1[val].append(key)
    for i in sorted(h1.keys()):
        if len(h1[i])>0:
            c=0
            l=list(sorted(h1[i]))
            while c!=len(l):
                print(i,l[c])
                c+=1
        else:
            print(i,*h1[i])
