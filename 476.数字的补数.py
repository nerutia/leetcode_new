'''
Author: your name
Date: 2021-04-25 16:37:14
LastEditTime: 2021-04-25 16:42:13
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \tmp\476.数字的补数.py
'''
#
# @lc app=leetcode.cn id=476 lang=python3
#
# [476] 数字的补数
#

# @lc code=start
class Solution:
    def findComplement(self, num: int) -> int:
        if num <= 0:
            return num
        t = 1
        while t <= num:
            t <<= 1
        return t - num - 1
# @lc code=end

