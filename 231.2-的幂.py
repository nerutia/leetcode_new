#
# @lc app=leetcode.cn id=231 lang=python3
#
# [231] 2的幂
#

# @lc code=start
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n < 1:
            return False
        while n > 1:
            if n & 1:
                return False
            n >>= 1
        return True
        # 大佬
        # return n > 0 and not (n & (n - 1))
# @lc code=end

