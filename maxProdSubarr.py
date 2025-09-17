class Solution:
	def maxProduct(self,arr):
		res = float('-inf')
		n = len(arr)
		p,s = 1,1
		
		for i in range(n):
		    if p == 0:
		        p = 1
		    if s == 0:
		        s = 1
		    p *= arr[i]
		    s *= arr[n-i-1]
		    res = max(res,max(p,s))
		    
		return res
		    
