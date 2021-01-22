#https://www.hackerearth.com/practice/data-structures/hash-tables/basics-of-hash-tables/practice-problems/algorithm/bob-and-string-easy/


'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
from collections import Counter
t=int(input())
for i in range(t):
    s=input()
    t=input()
    x=Counter(s)
    p=Counter(t)
    p=x&p
    res=0
    for key,val in p.items():
        res+=val*2
    print(len(s)+len(t)-res)
