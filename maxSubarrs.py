class Solution:
    def maxOfSubarrays(self, arr, k):
        n = len(arr)
        res = []

        if k == 1:
            return arr
        if k == n:
            return [max(arr)]

        
        curr_max = [max(arr[0:k]), arr.index(max(arr[0:k]))]
        res.append(curr_max[0])

        first = 1
        for i in range(k, n):
            if curr_max[1] < first:   
                curr_max = [max(arr[first:i+1]), first + arr[first:i+1].index(max(arr[first:i+1]))]
            else:
                if arr[i] > curr_max[0]:
                    curr_max = [arr[i], i]
            res.append(curr_max[0])
            first += 1

        return res
