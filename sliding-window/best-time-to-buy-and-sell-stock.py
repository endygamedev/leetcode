# Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock

# Time Complexity: O(n)
# Space Complexity: O(1)


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        l = 0
        for r in range(len(prices)):
            if prices[r] < prices[l]:
                l = r
            res = max(prices[r] - prices[l], res)
        return res
