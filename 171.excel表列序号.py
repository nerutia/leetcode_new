#
# @lc app=leetcode.cn id=171 lang=python3
#
# [171] Excel表列序号
#

# @lc code=start
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        l = list(columnTitle)
        r = 0
        for i in l:
            r *= 26
            v = ord(i) - ord('A')
            r += v + 1
        return r
# @lc code=end

