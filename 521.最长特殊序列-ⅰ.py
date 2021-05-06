'''
Description: 
Version: 1.0
Author: hqh
Date: 2021-05-02 01:14:23
LastEditors: hqh
LastEditTime: 2021-05-02 01:17:52
'''
#
# @lc app=leetcode.cn id=521 lang=python3
#
# [521] 最长特殊序列 Ⅰ
#

# @lc code=start
class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        if a == b:
            return -1
        return max(len(a), len(b))


# @lc code=end
