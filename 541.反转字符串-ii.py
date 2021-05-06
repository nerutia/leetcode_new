'''
Description: 
Version: 1.0
Author: hqh
Date: 2021-05-06 01:47:03
LastEditors: hqh
LastEditTime: 2021-05-06 13:14:50
'''
#
# @lc app=leetcode.cn id=541 lang=python3
#
# [541] 反转字符串 II
#

# @lc code=start
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        r = []
        for i in range(0, len(s), 2 * k):
            r.append(s[i : i + k][::-1])
            r.append(s[i + k : i + 2 * k])
        return ''.join(r)


# @lc code=end
