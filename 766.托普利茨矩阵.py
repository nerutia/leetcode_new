'''
Description: 
Version: 1.0
Author: hqh
Date: 2021-05-16 22:42:10
LastEditors: hqh
LastEditTime: 2021-05-16 22:53:15
'''
#
# @lc app=leetcode.cn id=766 lang=python3
#
# [766] 托普利茨矩阵
#

# @lc code=start
class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        a = len(matrix)
        b = len(matrix[0])
        for i in range(a):
            for j in range(i):
                matrix[i].insert(b, matrix[j][b - 1])
        for i in range(a):
            for j in range(i + 1, a):
                matrix[i].insert(0, matrix[j][0])
        for i in range(a - 1):
            if not matrix[i] == matrix[i + 1]:
                return False
        return True
        # 大佬
        # 只需判断：前行中除最后一个元素外剩余的元素完全等于后行中除第一个元素外剩余的元素。


# @lc code=end
