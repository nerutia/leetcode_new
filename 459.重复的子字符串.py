'''
Author: your name
Date: 2021-04-25 16:10:22
LastEditTime: 2021-04-25 16:22:11
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \tmp\459.重复的子字符串.py
'''
#
# @lc app=leetcode.cn id=459 lang=python3
#
# [459] 重复的子字符串
#

# @lc code=start
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        l = len(s)
        for i in range(1, l):
            if s == s[i:] + s[:i]:
                return True
        return False
        # 大佬：
        # return s in (s+s)[1:-1]
# @lc code=end

