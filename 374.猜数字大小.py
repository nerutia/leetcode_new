#
# @lc app=leetcode.cn id=374 lang=python3
#
# [374] 猜数字大小
#

# @lc code=start
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        l, r = 1, n + 1
        while l < r:
            m = l + (r - l) // 2
            if guess(m) == 0:
                return m
            elif guess(m) < 0:
                r = m
            else:
                l = m + 1
        return l
# @lc code=end

