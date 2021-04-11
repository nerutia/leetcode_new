#
# @lc app=leetcode.cn id=172 lang=python3
#
# [172] 阶乘后的零
#

# @lc code=start
class Solution:
    def trailingZeroes(self, n: int) -> int:
        # 本质是统计5的数量
        r = 0
        while n > 0:
            n //= 5 # 每次除以5后计算有多少个数即可，
            r += n # 这里其实是**恰好**加n
        return r
# @lc code=end

