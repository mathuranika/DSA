
class Solution:
    def isBalanced(self, s):
        pair  = {'(':')', '{':'}', '[':']'}
        stack = [0]
        
        for i in s:
            if i in pair.keys():
                stack.append(pair[i])
            elif i == stack[-1]:
                stack.pop()
            else:
                return False
        
        if stack == [0]:
            return True
        else:
            return False
