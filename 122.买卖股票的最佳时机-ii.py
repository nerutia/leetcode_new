#
# @lc app=leetcode.cn id=122 lang=python3
#
# [122] 买卖股票的最佳时机 II
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        return sum(max(0, prices[i+1] - prices[i]) for i in range(len(prices) - 1)) if len(prices) > 1 else 0
# @lc code=end

