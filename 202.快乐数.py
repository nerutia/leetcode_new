#
# @lc app=leetcode.cn id=202 lang=python3
#
# [202] 快乐数
#

# @lc code=start
class Solution:
    def isHappy(self, n: int) -> bool:
        s = {1}
        while n not in s:
            s.add(n)
            t = 0
            while n:
                t += (n % 10)**2
                n //= 10
            n = t
        return n == 1
# @lc code=end

