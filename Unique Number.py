#   https://codeforces.com/problemset/problem/1462/C



def fun(n):
	res=''
	for i in range(9,0,-1):
		if n>=i:
			n-=i
			res+=str(i)
	if len(res)==0 or n!=0:
		print(-1)
	else:
		print(res[::-1])

for i in range(int(input())):
	n=int(input())
	fun(n)


