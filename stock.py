from typing import List

class Solution:
    def maximumProfit(self, prices: List[int]) -> int:
        n = len(prices)
        i = 0
        res = 0

        while i < n - 1:
            # local minima (buy)
            while i < n - 1 and prices[i] >= prices[i + 1]:
                i += 1
            if i == n - 1:
                break
            buy = prices[i]
            i += 1

            # local maxima (sell)
            while i < n and prices[i] >= prices[i - 1]:
                i += 1
            sell = prices[i - 1]

            res += sell - buy

        return res
