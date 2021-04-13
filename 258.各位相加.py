#
# @lc app=leetcode.cn id=258 lang=python3
#
# [258] 各位相加
#

# @lc code=start
class Solution:
    def addDigits(self, num: int) -> int:
        # f(x*10+y)=f(x*9+x+y)=f(x+y), 成立当f(x)= x%9
        if num > 9:
            num = num % 9
            if num == 0:
                return 9
        return num
# @lc code=end

