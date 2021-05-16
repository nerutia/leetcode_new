'''
Description: 
Version: 1.0
Author: hqh
Date: 2021-05-16 21:36:57
LastEditors: hqh
LastEditTime: 2021-05-16 21:42:47
'''
#
# @lc app=leetcode.cn id=744 lang=python3
#
# [744] 寻找比目标字母大的最小字母
#

# @lc code=start
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        for idx, val in enumerate(letters):
            if target < val:
                return letters[idx]
        return letters[0]


# @lc code=end
