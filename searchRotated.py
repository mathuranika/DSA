class Solution:
    def search(self, arr, key):
        piv = arr.index(min(arr))   
        n = len(arr)

        if key == arr[piv]:
            return piv

        if key >= arr[piv] and key <= arr[n-1]:
            low, high = piv, n-1
        else:
            low, high = 0, piv-1

        while low <= high:
            mid = (low + high) // 2
            if arr[mid] == key:
                return mid
            elif arr[mid] > key:
                high = mid - 1
            else:
                low = mid + 1

        return -1
