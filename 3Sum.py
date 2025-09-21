# O(n2) time complexity
from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        n = len(nums)

        for i in range(0, n - 1):
            seen = []
            for j in range(i + 1, n):
                curr = [nums[i], nums[j]]
                c_sum = sum(curr)
                if -c_sum in seen:
                    triplet = tuple(sorted([nums[i], nums[j], -c_sum]))
                    res.add(triplet)
                seen.append(nums[j])

        return [list(triplet) for triplet in res]

#O(nlogn) Optimized
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        nums.sort()

        for i in range(0,n):
            if i>0 and nums[i] == nums[i-1]: 
                continue
            j = i+1
            k = n-1
            while j<k:
                Sum = nums[i]+nums[j]+nums[k]
                if Sum > 0:
                    k-=1
                elif Sum < 0:
                    j+=1
                else:
                    res.append([nums[i],nums[j],nums[k]])
                    j += 1
                    k -= 1
                    while j<k and nums[j] == nums[j-1]:
                        j += 1
                    while j<k and nums[k] == nums[k+1]:
                        k -= 1
        return res




