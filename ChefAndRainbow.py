#https://www.codechef.com/status/RAINBOWA,utkarsh_sri
def inc_sequence(arr, n):
    return set(arr[:n//2 + 1]) == {1,2,3,4,5,6,7}
def is_palindrome(arr, n):
    for i in range(n//2+1):
        if arr[i] != arr[n-i-1]:
            return False
    return True
for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    if inc_sequence(arr, n) and is_palindrome(arr, n):
        print("yes")
    else:
        print("no")
