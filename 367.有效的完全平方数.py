#
# @lc app=leetcode.cn id=367 lang=python3
#
# [367] 有效的完全平方数
#

# @lc code=start
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        r = num
        while r - num / r > 1:
            r = (num / r + r) / 2
        r = r // 1
        return r * r == num
        # 大佬
        # return num**0.5 % 1 == 0
# @lc code=end

