class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def fun(arr,start,end):
            while (start<=end):
                mid=(end+start)//2
                if arr[mid]==target:
                    return mid
                elif arr[start]<=arr[mid]:
                    if arr[start]<=target and arr[mid]>=target:
                        end=mid-1
                    else:
                        start=mid+1
                else:
                    if arr[mid]<=target and arr[end]>=target:
                        start=mid+1
                    else:
                        end=mid-1
            return -1
        return fun(nums,0,len(nums)-1)