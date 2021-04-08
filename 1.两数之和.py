#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s = {}
        for i in range(len(nums)):
            v = target - nums[i]
            if v in s:
                return s[v], i
            s[nums[i]] = i
# @lc code=end

