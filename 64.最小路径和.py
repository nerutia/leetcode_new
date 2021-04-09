#
# @lc app=leetcode.cn id=64 lang=python3
#
# [64] 最小路径和
#

# @lc code=start
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        x, y = len(grid), len(grid[0])
        for i in range(x):
            for j in range(y):
                if i == 0 and j == 0:
                    continue
                if i == 0:
                    grid[i][j]
# @lc code=end

