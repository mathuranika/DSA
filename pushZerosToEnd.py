class Solution:
	def pushZerosToEnd(self, arr):
	    n = len(arr)
    	i = 0
    	final = n-1
    	
    	while i<final:
    	    if arr[i] == 0:
    	        arr.insert(final+1,0)
    	        arr.pop(i)
    	        final -= 1
    	    else:
    	        i += 1
    	        
        return arr
    	        
    	    
