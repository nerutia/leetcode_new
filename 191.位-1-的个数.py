#
# @lc app=leetcode.cn id=191 lang=python3
#
# [191] 位1的个数
#

# @lc code=start
class Solution:
    def hammingWeight(self, n: int) -> int:
        r = 0
        while n:
            r += n & 1
            n >>= 1
        return r
# @lc code=end

