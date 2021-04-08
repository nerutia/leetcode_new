#
# @lc app=leetcode.cn id=13 lang=python3
#
# [13] 罗马数字转整数
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        def f(x):
            if x == 'I':
                return 1
            if x == 'V':
                return 5
            if x == 'X':
                return 10
            if x == 'L':
                return 50
            if x == 'C':
                return 100
            if x == 'D':
                return 500
            if x == 'M':
                return 1000
        r = 0
        t = map(f, s)
        for i in range(len(t) - 1):
            if t[i] < t[i+1]:
                t[i] = -t[i]
        return sum(t)
# @lc code=end

