# O(n2) complexity
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
