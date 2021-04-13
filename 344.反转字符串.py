#
# @lc app=leetcode.cn id=344 lang=python3
#
# [344] 反转字符串
#

# @lc code=start
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l = len(s)
        for i in range(l//2):
            s[i], s[l-1-i] = s[l-1-i], s[i]
        return s
        # 使用位操作来交换数据不需要额外空间：
        # s[i] ^= s[j]
        # s[j] ^= s[i]
        # s[i] ^= s[j]
# @lc code=end

