#  https://mycode.prepbytes.com/problems/arrays/DICEGM1



t=int(input())
for i in range(t):
  n=int(input())
  arr=list(int(x) for x in input().split())
  res1=0
  res2=0
  f=0
  for i in range(len(arr)):
    if i%2==0 and arr[i]%2==0:
      res1+=1
    elif i%2!=0 and arr[i]%2==0:
      res2+=1
  if res1==res2:
    print("Ben")
  elif res1>res2:
    print("Ben")
  else:
    print("Jim")
