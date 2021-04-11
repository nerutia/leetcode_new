#
# @lc app=leetcode.cn id=204 lang=python3
#
# [204] 计数质数
#

# @lc code=start
class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 3:
            return 0
        r = [0] * n
        s = 0
        for i in range(2, n):
            if r[i] == 0:
                s += 1
                for j in range(i, n, i):
                    r[j] = 1
        return s
# @lc code=end

