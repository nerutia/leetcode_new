'''
Description: 
Version: 1.0
Author: hqh
Date: 2021-05-08 01:16:00
LastEditors: hqh
LastEditTime: 2021-05-09 00:23:27
'''
#
# @lc app=leetcode.cn id=598 lang=python3
#
# [598] 范围求和 II
#

# @lc code=start
class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        a, b = m, n
        for op in ops:
            a = min(a, op[0])
            b = min(b, op[1])
        return a * b


# @lc code=end
