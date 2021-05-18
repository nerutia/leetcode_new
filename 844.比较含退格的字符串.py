'''
Description: 
Version: 1.0
Author: hqh
Date: 2021-05-18 22:18:37
LastEditors: hqh
LastEditTime: 2021-05-18 22:26:05
'''
#
# @lc app=leetcode.cn id=844 lang=python3
#
# [844] 比较含退格的字符串
#

# @lc code=start
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        r1 = []
        for i in s:
            if i == '#':
                if r1:
                    r1.pop()
            else:
                r1.append(i)
        r2 = []
        for i in t:
            if i == '#':
                if r2:
                    r2.pop()
            else:
                r2.append(i)
        return r1 == r2


# @lc code=end
