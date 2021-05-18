'''
Description: 
Version: 1.0
Author: hqh
Date: 2021-05-18 10:04:06
LastEditors: hqh
LastEditTime: 2021-05-18 10:09:17
'''
#
# @lc app=leetcode.cn id=796 lang=python3
#
# [796] 旋转字符串
#

# @lc code=start
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        if s == "":
            return True
        for i in range(len(s)):
            if s[i:] + s[:i] == goal:
                return True
        return False


# @lc code=end
