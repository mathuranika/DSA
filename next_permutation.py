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
