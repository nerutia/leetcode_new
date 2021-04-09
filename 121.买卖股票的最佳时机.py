#
# @lc app=leetcode.cn id=121 lang=python3
#
# [121] 买卖股票的最佳时机
#
from typing import List
# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        m = [prices[0]]
        r = prices[1] - prices[0]
        for i in range(1, len(prices)):
            m.append(min(m[i-1], prices[i]))
            r = max(r, prices[i] - m[i])
        return r
# @lc code=end
c = Solution()
print(c.maxProfit([7,1,5,3,6,4]))
