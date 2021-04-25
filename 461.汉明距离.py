'''
Author: your name
Date: 2021-04-25 16:30:07
LastEditTime: 2021-04-25 16:33:15
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \tmp\461.汉明距离.py
'''
#
# @lc app=leetcode.cn id=461 lang=python3
#
# [461] 汉明距离
#

# @lc code=start
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        r = 0
        while x or y:
            r += (x ^ y) & 1
            x >>= 1
            y >>= 1
        return r
        # 大佬
        # return bin(x ^ y).count('1')
# @lc code=end

