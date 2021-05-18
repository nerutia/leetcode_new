'''
Description: 
Version: 1.0
Author: hqh
Date: 2021-05-18 10:26:58
LastEditors: hqh
LastEditTime: 2021-05-18 10:53:43
'''
#
# @lc app=leetcode.cn id=806 lang=python3
#
# [806] 写字符串需要的行数
#

# @lc code=start
class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        t = 0
        c = 0
        for i in s:
            idx = ord(i) - ord('a')
            if t + widths[idx] > 100:
                c += 1
                t = widths[idx]
            else:
                t += widths[idx]
        if t > 0:
            c += 1
        return [c, t]


# @lc code=end
