'''
Author: your name
Date: 2021-04-25 16:36:27
LastEditTime: 2021-04-25 16:37:07
LastEditors: your name
Description: In User Settings Edit
FilePath: \tmp\463.岛屿的周长.py
'''
#
# @lc app=leetcode.cn id=463 lang=python3
#
# [463] 岛屿的周长
#

# @lc code=start
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        r = 0
        a,b = len(grid), len(grid[0])
        for i in range(a):
            for j in range(b):
                if grid[i][j] == 1:
                    if i == 0 or grid[i-1][j] == 0:
                        r += 1
                    if j == 0 or grid[i][j-1] == 0:
                        r += 1
                    if i == a-1 or grid[i+1][j] == 0:
                        r += 1
                    if j == b-1 or grid[i][j+1] == 0:
                        r += 1
        return r
# @lc code=end

