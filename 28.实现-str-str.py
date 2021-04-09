#
# @lc app=leetcode.cn id=28 lang=python3
#
# [28] 实现 strStr()
#

# @lc code=start
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        l = len(haystack)
        m = len(needle)
        if l < m:
            return -1
        if m == 0:
            return 0
        for i in range(l-m+1):
            if haystack[i:i+m] == needle:
                return i
        return -1
# @lc code=end

