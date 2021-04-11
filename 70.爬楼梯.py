#
# @lc app=leetcode.cn id=70 lang=python3
#
# [70] 爬楼梯
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        l = [0] * (n + 3)
        l[1] = 1
        l[2] = 2
        if n < 3:
            return l[n]
        for i in range(3, n + 1):
            l[i] = l[i-1] + l[i-2]
        return l[n]
# @lc code=end

