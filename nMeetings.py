#User function Template for python3

class Solution:
    
    #Function to find the maximum number of meetings that can
    #be performed in a meeting room.
    def maximumMeetings(self,start,end):
        res = 1
        n = len(start)
        
        se = sorted(zip(start,end), key=lambda x: x[1])
        
        time = se[0][1]
        
        for j in range(1,n):
            if se[j][0] > time:
                res+=1
                time = se[j][1]
        
        return res
            
        
