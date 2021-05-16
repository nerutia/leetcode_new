'''
Description: 
Version: 1.0
Author: hqh
Date: 2021-05-16 22:29:05
LastEditors: hqh
LastEditTime: 2021-05-16 22:41:32
'''
#
# @lc app=leetcode.cn id=762 lang=python3
#
# [762] 二进制表示中质数个计算置位
#

# @lc code=start
class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        r = 0
        for i in range(left, right + 1):
            t = 0
            while i:
                t += i & 1
                i >>= 1
            if t in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]:
                r += 1
        return r


# @lc code=end
