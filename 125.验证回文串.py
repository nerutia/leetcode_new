#
# @lc app=leetcode.cn id=125 lang=python3
#
# [125] 验证回文串
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        r = []
        for i in s:
            if i.isalnum():
                r.append(i.lower())
        # return r
        return r == r[::-1]
# @lc code=end

