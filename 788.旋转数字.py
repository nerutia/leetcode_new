'''
Description: 
Version: 1.0
Author: hqh
Date: 2021-05-16 23:26:45
LastEditors: hqh
LastEditTime: 2021-05-16 23:33:16
'''
#
# @lc app=leetcode.cn id=788 lang=python3
#
# [788] 旋转数字
#

# @lc code=start
class Solution:
    def rotatedDigits(self, n: int) -> int:
        r = 0
        for i in range(1, n + 1):
            if self.isf(i):
                r += 1
        return r

    def isf(self, n):
        f = False
        while n:
            t = n % 10
            n //= 10
            if t in [0, 1, 8]:
                continue
            if t in [2, 5, 6, 9]:
                f = True
                continue
            return False
        return f


# @lc code=end
