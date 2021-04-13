#
# @lc app=leetcode.cn id=342 lang=python3
#
# [342] 4的幂
#

# @lc code=start
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n < 1:
            return False
        if n & (n-1):  # 关键，检查是不是只有一位是1，也就是2的幂
            return False
        return n % 3 == 1  # 确定是4的倍数
        # 也可以return n & 0x55555555
# @lc code=end

