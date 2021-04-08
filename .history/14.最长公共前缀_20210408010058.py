#
# @lc app=leetcode.cn id=14 lang=python3
#
# [14] 最长公共前缀
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        r = ""
        ml = min(map(len, strs))
        for i in range(len(strs)):
            for j in range(ml):
                
# @lc code=end

