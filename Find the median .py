class Solution:
	def find_median(self, v):
		# Code here
		arr=v
		arr.sort()
		if len(arr)%2!=0:
	    	return arr[len(arr)//2]
	    else:
	        return arr[len(arr)//2]
