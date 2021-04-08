#
# @lc app=leetcode.cn id=7 lang=python3
#
# [7] 整数反转
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        s = -1 if x < 0 else 1
        x = abs(x)
        r = 0
        while x:
            r *= 10
            r += x % 10
            x //= 10
        return s * r
# @lc code=end

