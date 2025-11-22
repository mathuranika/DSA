class Solution:
    def swap(self, arr, i, j):
        arr[i], arr[j] = arr[j], arr[i]

    def nextPermutation(self, arr):
        n = len(arr)
        fix_ind = -1  # To track if we found a valid pivot
        
        for i in range(n - 2, -1, -1):
            a = arr[i]
            min_diff = float('inf') 
            ind = -1
            for j in range(i + 1, n):
                if arr[j] > a and arr[j] - a < min_diff:
                    min_diff = arr[j] - a
                    ind = j
            if ind != -1:
                fix_ind = i
                self.swap(arr, fix_ind, ind)
                break

        if fix_ind == -1:
            arr.sort()
        else:
            arr[fix_ind + 1:] = sorted(arr[fix_ind + 1:])

        return arr


## Leetcode

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        n = len(nums)
        piv = None

        for i in range(n-2, -1, -1):
            if nums[i] < nums[i+1]:
                piv = i
                break

        if piv is None:
            nums.reverse()
            return nums

        min_ind = piv + 1
        for j in range(piv+1, n):
            if nums[j] > nums[piv] and nums[j] <= nums[min_ind]:
                min_ind = j

        nums[piv], nums[min_ind] = nums[min_ind], nums[piv]

        arr_sort = nums[piv+1:]
        arr_sort.sort()

        k = piv + 1
        l = 0
        while k < n:
            nums[k] = arr_sort[l]
            k += 1
            l += 1

        return nums
