#
# @lc app=leetcode.cn id=168 lang=python3
#
# [168] Excel表列名称
#

# @lc code=start
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        r = []
        while columnNumber:
            columnNumber -= 1
            r.append(chr(ord('A') + columnNumber % 26))
            columnNumber //= 26
        return ''.join(r[::-1])
# @lc code=end
