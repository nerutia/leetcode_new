'''
Description: 
Version: 1.0
Author: hqh
Date: 2021-05-15 21:54:49
LastEditors: hqh
LastEditTime: 2021-05-15 22:17:20
'''
#
# @lc app=leetcode.cn id=696 lang=python3
#
# [696] 计数二进制子串
#

# @lc code=start
class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        r = 0
        r1, r2 = 0, 1
        for i in range(len(s) - 1):
            if s[i] == s[i + 1]:
                r2 += 1
            else:
                r += min(r1, r2)
                r1 = r2
                r2 = 1
        r += min(r1, r2)
        return r


# @lc code=end
