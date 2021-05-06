'''
Description: 
Version: 1.0
Author: hqh
Date: 2021-05-06 13:27:28
LastEditors: hqh
LastEditTime: 2021-05-06 13:28:37
'''
#
# @lc app=leetcode.cn id=557 lang=python3
#
# [557] 反转字符串中的单词 III
#

# @lc code=start
class Solution:
    def reverseWords(self, s: str) -> str:
        st = s.split(' ')
        for i in range(len(st)):
            st[i] = st[i][::-1]
        return ' '.join(st)


# @lc code=end
