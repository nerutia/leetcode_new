#
# @lc app=leetcode.cn id=268 lang=python3
#
# [268] 丢失的数字
#

# @lc code=start
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # 问唯一想异或
        r = len(nums)
        for i in range(len(nums)):
            r ^= nums[i] ^ i
        return r
# @lc code=end

