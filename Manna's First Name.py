# https://www.hackerearth.com/practice/algorithms/searching/linear-search/practice-problems/algorithm/mannas-first-name-4/description/


'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
for i in range(int(input())):
    s=input()
    p=(s.count("SUVOJIT"))
    s=s.replace("SUVOJIT","")
    print("SUVO =",str(s.count("SUVO"))+",","SUVOJIT =",p)
