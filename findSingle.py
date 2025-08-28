#User function Template for python3

class Solution:
    def findSingle(self, arr):
        unq = []
        for i in arr:
            if i in unq:
                unq.pop(unq.index(i))
            else:
                unq.append(i)
        return unq[0]
