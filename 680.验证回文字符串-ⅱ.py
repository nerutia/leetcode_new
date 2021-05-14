'''
Description: 
Version: 1.0
Author: hqh
Date: 2021-05-14 10:11:53
LastEditors: hqh
LastEditTime: 2021-05-14 11:24:59
'''
#
# @lc app=leetcode.cn id=680 lang=python3
#
# [680] 验证回文字符串 Ⅱ
#

# @lc code=start
class Solution:
    def validPalindrome(self, s: str) -> bool:
        l = len(s)
        for i in range(l // 2 + 1):
            if s[i] == s[l - i - 1]:
                continue
            return self.isP(s[i + 1 : l - i]) or self.isP(s[i : l - i - 1])
        return True

    def isP(self, s):
        return s == s[::-1]


# @lc code=end
