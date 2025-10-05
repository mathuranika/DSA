class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        n = len(nums)
        for i in range(n):
            find = target-nums[i]
            if find in seen.keys():
                return [seen[find],i]
            seen[nums[i]] = i
            
        
