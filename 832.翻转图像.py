'''
Description: 
Version: 1.0
Author: hqh
Date: 2021-05-18 21:32:41
LastEditors: hqh
LastEditTime: 2021-05-18 21:36:44
'''
#
# @lc app=leetcode.cn id=832 lang=python3
#
# [832] 翻转图像
#

# @lc code=start
class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        return [[1 - i for i in img[::-1]] for img in image]


# @lc code=end
