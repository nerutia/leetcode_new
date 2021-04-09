#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        for i in s:
            if i == '(' or i == '[' or i == '{':
                st.append(i)
            if i == ')':
                if st != [] and st[-1] == '(':
                    st.pop()
                else:
                    return False
            if i == ']':
                if st != [] and st[-1] == '[':
                    st.pop()
                else:
                    return False
            if i == '}':
                if st != [] and st[-1] == '{':
                    st.pop()
                else:
                    return False
        return st == []

# @lc code=end

