#https://www.codechef.com/problems/VALIDSTK

# cook your dish here
for i in range(int(input())):
    n=int(input())
    arr=list(int(x) for x in input().split())
    def valid(arr):
        c=0
        k=0
        m=0
        l=[]
        for i in range(len(arr)):
            if arr[i]==1:
               c+=1
            else:
                c-=1
            if c<0:
                print("Invalid")
                break
        else:
            print("Valid")
    valid(arr)
            
         
