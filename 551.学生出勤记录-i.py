'''
Description: 
Version: 1.0
Author: hqh
Date: 2021-05-06 13:22:21
LastEditors: hqh
LastEditTime: 2021-05-06 13:27:17
'''
#
# @lc app=leetcode.cn id=551 lang=python3
#
# [551] 学生出勤记录 I
#

# @lc code=start
class Solution:
    def checkRecord(self, s: str) -> bool:
        r = 1
        f = 2
        for i in s:
            if i == 'A':
                r -= 1
                if r < 0:
                    return False
                f = 2
            if i == 'L':
                f -= 1
                if f < 0:
                    return False
            if i == 'P':
                f = 2
        return True


# @lc code=end
