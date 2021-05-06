'''
Description: 
Version: 1.0
Author: hqh
Date: 2021-05-06 13:45:50
LastEditors: hqh
LastEditTime: 2021-05-06 13:48:48
'''
#
# @lc app=leetcode.cn id=566 lang=python3
#
# [566] 重塑矩阵
#

# @lc code=start
class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        size = len(mat) * len(mat[0])
        if size != r * c:
            return mat
        t = []
        for i in mat:
            t += i
        r = []
        for i in range(0, size, c):
            r.append(t[i : i + c])
        return r


# @lc code=end
