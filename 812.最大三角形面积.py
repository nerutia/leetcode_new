'''
Description: 
Version: 1.0
Author: hqh
Date: 2021-05-18 11:48:29
LastEditors: hqh
LastEditTime: 2021-05-18 13:28:00
'''
#
# @lc app=leetcode.cn id=812 lang=python3
#
# [812] 最大三角形面积
#

# @lc code=start
class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        self.p = points
        r = 0
        l = len(points)
        for i in range(l - 2):
            for j in range(i + 1, l - 1):
                for k in range(j + 1, l):
                    v = self.dim(i, j, k)
                    r = max(r, v)
        return r

    def dim(self, i, j, k):
        x1 = self.p[i][0]
        y1 = self.p[i][1]
        x2 = self.p[j][0]
        y2 = self.p[j][1]
        x3 = self.p[k][0]
        y3 = self.p[k][1]
        return abs((x1 - x3) * (y2 - y3) - (x2 - x3) * (y1 - y3)) / 2.0


# @lc code=end
