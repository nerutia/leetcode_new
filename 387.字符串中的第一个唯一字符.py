#
# @lc app=leetcode.cn id=387 lang=python3
#
# [387] 字符串中的第一个唯一字符
#

# @lc code=start
class Solution:
    def firstUniqChar(self, s: str) -> int:
        st = set()
        for i in range(len(s)):
            if s[i] in st:
                continue
            st.add(s[i])
            if s[i] in s[i+1:]:
                continue
            return i
        return -1
# @lc code=end

