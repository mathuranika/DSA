#User function Template for python3
class Solution:
	def removeDups(self, str):
		seen = []
		new = ""
		for i in str:
		    if i not in seen:
		        new += i
		        seen.append(i)
		return new
