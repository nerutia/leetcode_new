'''
Description: 
Version: 1.0
Author: hqh
Date: 2021-05-11 10:59:11
LastEditors: hqh
LastEditTime: 2021-05-11 13:08:13
'''
#
# @lc app=leetcode.cn id=661 lang=python3
#
# [661] 图片平滑器
#

# @lc code=start
class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        r, c = len(img), len(img[0])
        res = []
        for i in range(r):
            t = []
            for j in range(c):
                t.append(self.calc(img, i, j, r, c))
            res.append(t)
        return res

    def calc(self, img, i, j, r, c):
        d = 0
        v1, v2, v3, v4, v5, v6, v7, v8, v9 = 0, 0, 0, 0, 0, 0, 0, 0, 0
        if i > 0 and j > 0:
            v1, d = img[i - 1][j - 1], d + 1
        if i > 0:
            v2, d = img[i - 1][j], d + 1
        if i > 0 and j < c - 1:
            v3, d = img[i - 1][j + 1], d + 1
        if j > 0:
            v4, d = img[i][j - 1], d + 1
        v5, d = img[i][j], d + 1
        if j < c - 1:
            v6, d = img[i][j + 1], d + 1
        if i < r - 1 and j > 0:
            v7, d = img[i + 1][j - 1], d + 1
        if i < r - 1:
            v8, d = img[i + 1][j], d + 1
        if i < r - 1 and j < c - 1:
            v9, d = img[i + 1][j + 1], d + 1
        return (v1 + v2 + v3 + v4 + v5 + v6 + v7 + v8 + v9) // d


# @lc code=end
