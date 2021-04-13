#
# @lc app=leetcode.cn id=383 lang=python3
#
# [383] 赎金信
#

# @lc code=start
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        l = list(magazine)
        for i in ransomNote:
            if i in l:
                l.remove(i)
            else:
                return False
        return True
# @lc code=end

