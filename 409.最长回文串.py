#
# @lc app=leetcode.cn id=409 lang=python3
#
# [409] 最长回文串
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> int:
        r = 0
        st = set()
        for i in s:
            if i in st:
                st.remove(i)
                r += 2
            else:
                st.add(i)
        if st:
            return r + 1
        return r
# @lc code=end

