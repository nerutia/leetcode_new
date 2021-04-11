#
# @lc app=leetcode.cn id=190 lang=python3
#
# [190] 颠倒二进制位
#

# @lc code=start
class Solution:
    def reverseBits(self, n: int) -> int:
        t = 0
        c = 32
        while c:
            t <<= 1
            t += n % 2
            n >>= 1
            c -= 1
        return t
# @lc code=end

