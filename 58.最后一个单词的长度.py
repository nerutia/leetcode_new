#
# @lc app=leetcode.cn id=58 lang=python3
#
# [58] 最后一个单词的长度
#

# @lc code=start
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len((s.strip()+'a').split(' ')[-1]) - 1
        # return len(s.rstrip().split(' ')[-1])
# @lc code=end

