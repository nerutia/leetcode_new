#
# @lc app=leetcode.cn id=119 lang=python3
#
# [119] 杨辉三角 II
#

# @lc code=start
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        r = [1]
        while rowIndex > 0:
            for i in range(len(r) - 1, 0, -1):
                r[i] += r[i-1]
            r += [1]
            rowIndex -= 1
        return r
# @lc code=end

