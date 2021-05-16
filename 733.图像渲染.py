'''
Description: 
Version: 1.0
Author: hqh
Date: 2021-05-16 21:08:22
LastEditors: hqh
LastEditTime: 2021-05-16 21:34:34
'''
#
# @lc app=leetcode.cn id=733 lang=python3
#
# [733] 图像渲染
#

# @lc code=start
class Solution:
    def floodFill(
        self, image: List[List[int]], sr: int, sc: int, newColor: int
    ) -> List[List[int]]:
        self.img = image
        self.color = newColor
        self.oldColor = self.img[sr][sc]
        if self.oldColor == newColor:
            return self.img
        self.draw(sr, sc)
        return self.img

    def draw(self, x, y):
        self.img[x][y] = self.color
        if x > 0 and self.img[x - 1][y] == self.oldColor:
            self.draw(x - 1, y)
        if y > 0 and self.img[x][y - 1] == self.oldColor:
            self.draw(x, y - 1)
        if x < len(self.img) - 1 and self.img[x + 1][y] == self.oldColor:
            self.draw(x + 1, y)
        if y < len(self.img[0]) - 1 and self.img[x][y + 1] == self.oldColor:
            self.draw(x, y + 1)


# @lc code=end
