'''
Author: your name
Date: 2021-04-25 20:55:30
LastEditTime: 2021-04-25 21:00:21
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \tmp\504.七进制数.py
'''
#
# @lc app=leetcode.cn id=504 lang=python3
#
# [504] 七进制数
#

# @lc code=start
class Solution:
    def convertToBase7(self, num: int) -> str:
        if num < 0:
            pre = '-'
            num = -num
        elif num == 0:
            return '0'
        else:
            pre = ''
        r = []
        while num:
            r.append(str(num%7))
            num //= 7
        return pre + ''.join(r)[::-1]
# @lc code=end

