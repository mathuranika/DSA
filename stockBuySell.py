class Solution:
    #Function to find the days of buying and selling stock for max profit.
	def stockBuySell(self, arr):
        n = len(arr)
        i = 0
        res = 0

        while i < n - 1:
            while i < n - 1 and arr[i] >=arr[i + 1]:
                i += 1
            if i == n - 1:
                break
            buy = arr[i]
            i += 1

            while i < n and arr[i] >= arr[i - 1]:
                i += 1
            sell = arr[i - 1]

            res += sell - buy

        return res
