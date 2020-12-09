t=int(input())
for i in range(t):
  c=0
  n,k=map(int,input().split())
  arr=[int(x) for x in input().split()]
  for j in range(len(arr)):
      a=sum(arr)
      if arr[j]+k>a-arr[j]:
          c+=1
  print(c)
