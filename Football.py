#https://www.codechef.com/problems/MSNSADM1
# cook your dish here
def sum(arr1,arr2,n):	
    l=[]
    for i in range(n):
        s=(arr1[i]*20-arr2[i]*10)
        if s<0:
            l.append(0)
        else:
            l.append(s)
    return max(l)
	
t=int(input())
for i in range(t):
	n=int(input())
	arr1=list(int(x) for x in input().split())
	arr2=list(int(x) for x in input().split())
	print(sum(arr1,arr2,n))