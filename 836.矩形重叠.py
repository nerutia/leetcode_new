'''
Description: 
Version: 1.0
Author: hqh
Date: 2021-05-18 21:38:22
LastEditors: hqh
LastEditTime: 2021-05-18 22:18:24
'''
#
# @lc app=leetcode.cn id=836 lang=python3
#
# [836] 矩形重叠
#

# @lc code=start
class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        # 大佬
        # 将问题转为一维区间相交问题
        # 即区间最大左边界和最小右边界是否不重合
        return max(rec1[0], rec2[0]) < min(rec1[2], rec2[2]) and max(
            rec1[1], rec2[1]
        ) < min(rec1[3], rec2[3])


# @lc code=end
